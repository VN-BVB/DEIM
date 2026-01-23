"""
Copyright (c) 2024 The D-FINE Authors. All Rights Reserved.
"""

import tensorrt as trt
import torch
import torch.nn as nn
import torchvision.transforms as T

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from collections import OrderedDict

import sys
import os
import cv2  # Added for video processing
import tqdm
import contextlib
import collections
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from engine.extre_module.utils import increment_path
from engine.logger_module import get_logger
from tools.inference.utils import draw

logger = get_logger(__name__)

RED, GREEN, BLUE, YELLOW, ORANGE, RESET = "\033[91m", "\033[92m", "\033[94m", "\033[93m", "\033[38;5;208m", "\033[0m"
CLASS_NAME = None # Visdrone

# draw函数移植到 tools/inference/utils.py 文件内

class TimeProfiler(contextlib.ContextDecorator):
    def __init__(self):
        self.total = 0

    def __enter__(self):
        self.start = self.time()
        return self

    def __exit__(self, type, value, traceback):
        self.total += self.time() - self.start

    def reset(self):
        self.total = 0

    def time(self):
        if torch.cuda.is_available():
            torch.cuda.synchronize()
        return time.time()

class TRTInference(object):
    def __init__(self, engine_path, device='cuda:0', backend='torch', max_batch_size=32, verbose=False):
        self.engine_path = engine_path
        self.device = device
        self.backend = backend
        self.max_batch_size = max_batch_size

        self.logger = trt.Logger(trt.Logger.VERBOSE) if verbose else trt.Logger(trt.Logger.INFO)

        self.engine = self.load_engine(engine_path)
        self.context = self.engine.create_execution_context()
        self.bindings = self.get_bindings(self.engine, self.context, self.max_batch_size, self.device)
        self.bindings_addr = OrderedDict((n, v.ptr) for n, v in self.bindings.items())
        self.input_names = self.get_input_names()
        self.output_names = self.get_output_names()
        self.time_profile = TimeProfiler()

    def load_engine(self, path):
        trt.init_libnvinfer_plugins(self.logger, '')
        with open(path, 'rb') as f, trt.Runtime(self.logger) as runtime:
            return runtime.deserialize_cuda_engine(f.read())

    def get_input_names(self):
        names = []
        for _, name in enumerate(self.engine):
            if self.engine.get_tensor_mode(name) == trt.TensorIOMode.INPUT:
                names.append(name)
        return names

    def get_output_names(self):
        names = []
        for _, name in enumerate(self.engine):
            if self.engine.get_tensor_mode(name) == trt.TensorIOMode.OUTPUT:
                names.append(name)
        return names

    def get_bindings(self, engine, context, max_batch_size=32, device=None) -> OrderedDict:
        Binding = collections.namedtuple('Binding', ('name', 'dtype', 'shape', 'data', 'ptr'))
        bindings = OrderedDict()

        for i, name in enumerate(engine):
            shape = engine.get_tensor_shape(name)
            dtype = trt.nptype(engine.get_tensor_dtype(name))
            print(f"[ENGINE IO] {name}: shape={shape}, dtype={dtype}")
            if shape[0] == -1:
                shape[0] = max_batch_size
                if engine.get_tensor_mode(name) == trt.TensorIOMode.INPUT:
                    context.set_input_shape(name, shape)

            data = torch.from_numpy(np.empty(shape, dtype=dtype)).to(device)
            bindings[name] = Binding(name, dtype, shape, data, data.data_ptr())

        return bindings

    def run_torch(self, blob):
        for n in self.input_names:
            if self.bindings[n].shape != blob[n].shape:
                self.context.set_input_shape(n, blob[n].shape)
                self.bindings[n] = self.bindings[n]._replace(shape=blob[n].shape)

            assert self.bindings[n].data.dtype == blob[n].dtype, '{} dtype mismatch'.format(n)

        self.bindings_addr.update({n: blob[n].data_ptr() for n in self.input_names})
        self.context.execute_v2(list(self.bindings_addr.values()))
        outputs = {n: self.bindings[n].data for n in self.output_names}

        return outputs

    def __call__(self, blob):
        if self.backend == 'torch':
            return self.run_torch(blob)
        else:
            raise NotImplementedError("Only 'torch' backend is implemented.")

    def synchronize(self):
        if self.backend == 'torch' and torch.cuda.is_available():
            torch.cuda.synchronize()

def process_image(model, device, file_path, output_path, thrh):
    # 测量前处理时间
    preprocess_start = time.time()
    
    im_pil = Image.open(file_path).convert('RGB')
    w, h = im_pil.size
    orig_size = torch.tensor([[w, h]],dtype=torch.int32).to(device)

    transforms = T.Compose([
        T.Resize((640, 640)),
        T.ToTensor(),
    ])
    im_data = transforms(im_pil).unsqueeze(0)

    blob = {
        'images': im_data.to(device),
        'orig_target_sizes': orig_size.to(device),
    }
    
    model.synchronize()
    preprocess_time = time.time() - preprocess_start
    
    # 测量推理时间
    inference_start = time.time()
    output = model(blob)
    model.synchronize()
    inference_time = time.time() - inference_start
    
    # 测量后处理时间
    postprocess_start = time.time()
    labels, boxes, scores = output['labels'], output['boxes'], output['scores']
    im_pil = draw([im_pil], labels, boxes, scores, thrh=thrh, class_name=CLASS_NAME)
    im_pil.save(output_path / os.path.basename(file_path))
    postprocess_time = time.time() - postprocess_start
    
    # 计算总时间
    total_time = preprocess_time + inference_time + postprocess_time
    
    # 输出详细时间
    file_name = os.path.basename(file_path)
    print(f"\nImage: {file_name}")
    print(f"  Preprocessing: {preprocess_time*1000:.2f} ms")
    print(f"  Inference:     {inference_time*1000:.2f} ms")
    print(f"  Postprocessing:{postprocess_time*1000:.2f} ms")
    print(f"  Total:         {total_time*1000:.2f} ms ({1/total_time:.2f} FPS)")
    
    # 返回各阶段时间，用于统计平均值
    return preprocess_time, inference_time, postprocess_time, total_time

def process_video(model, device, file_path, output_path, thrh):
    cap = cv2.VideoCapture(file_path)

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    orig_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    orig_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path / os.path.basename(file_path), fourcc, fps, (orig_w, orig_h))

    transforms = T.Compose([
        T.Resize((640, 640)),
        T.ToTensor(),
    ])

    if cap.isOpened():
        total_preprocess_time = 0
        total_inference_time = 0
        total_postprocess_time = 0
        total_total_time = 0
        frame_count = 0
        
        for _ in tqdm.tqdm(range(total_frames), desc='Processing video frames...'):
            ret, frame = cap.read()
            if not ret:
                break

            # Convert frame to PIL image
            frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # 测量前处理时间
            preprocess_start = time.time()
            w, h = frame_pil.size
            orig_size = torch.tensor([[w, h]],dtype=torch.int32).to(device)
            im_data = transforms(frame_pil).unsqueeze(0)
            blob = {
                'images': im_data.to(device),
                'orig_target_sizes': orig_size.to(device),
            }
            model.synchronize()
            preprocess_time = time.time() - preprocess_start
            
            # 测量推理时间
            inference_start = time.time()
            output = model(blob)
            model.synchronize()
            inference_time = time.time() - inference_start
            
            # 测量后处理时间
            postprocess_start = time.time()
            labels, boxes, scores = output['labels'], output['boxes'], output['scores']
            frame_pil = draw([frame_pil], labels, boxes, scores, thrh=thrh, class_name=CLASS_NAME)
            frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)
            out.write(frame)
            postprocess_time = time.time() - postprocess_start
            
            # 累计时间
            total_preprocess_time += preprocess_time
            total_inference_time += inference_time
            total_postprocess_time += postprocess_time
            total_total_time += preprocess_time + inference_time + postprocess_time
            frame_count += 1
            
            # 每10帧输出一次平均时间
            if frame_count % 10 == 0:
                avg_preprocess = total_preprocess_time / frame_count
                avg_inference = total_inference_time / frame_count
                avg_postprocess = total_postprocess_time / frame_count
                avg_total = total_total_time / frame_count
                print(f"\nVideo Frame {frame_count}/{total_frames} - Average Times:")
                print(f"  Preprocessing: {avg_preprocess*1000:.2f} ms")
                print(f"  Inference:     {avg_inference*1000:.2f} ms")
                print(f"  Postprocessing:{avg_postprocess*1000:.2f} ms")
                print(f"  Total:         {avg_total*1000:.2f} ms ({1/avg_total:.2f} FPS)")

        # 输出视频总推理统计
        if frame_count > 0:
            avg_preprocess = total_preprocess_time / frame_count
            avg_inference = total_inference_time / frame_count
            avg_postprocess = total_postprocess_time / frame_count
            avg_total = total_total_time / frame_count
            print(f"\nVideo Processing Complete - Total Frames: {frame_count}")
            print(f"Average Times:")
            print(f"  Preprocessing: {avg_preprocess*1000:.2f} ms")
            print(f"  Inference:     {avg_inference*1000:.2f} ms")
            print(f"  Postprocessing:{avg_postprocess*1000:.2f} ms")
            print(f"  Total:         {avg_total*1000:.2f} ms ({1/avg_total:.2f} FPS)")
            print(f"Total Processing Time: {total_total_time:.2f} seconds")

    cap.release()
    out.release()


def main(args):
    global CLASS_NAME
    """Main function"""

    output_path = increment_path(args.output)
    logger.info(RED  + f"output_dir:{str(output_path)}" + RESET)
    output_path.mkdir(parents=True, exist_ok=True)

    device = args.device
    model = TRTInference(args.path, device=device)

    # Check if the input file is an image or a video
    file_path = args.input
    if os.path.isdir(file_path):
        total_preprocess_time = 0
        total_inference_time = 0
        total_postprocess_time = 0
        total_total_time = 0
        image_count = 0
        
        for file_name in tqdm.tqdm(os.listdir(file_path), desc=f'Process {file_path} folder'):
            if os.path.splitext(file_name)[-1].lower() in ['.jpg', '.jpeg', '.png', '.bmp']:
                # 调用process_image并获取各阶段时间
                pre_time, inf_time, post_time, total_time = process_image(
                    model, device, os.path.join(file_path, file_name), output_path, args.thrh
                )
                
                # 累计各阶段时间
                total_preprocess_time += pre_time
                total_inference_time += inf_time
                total_postprocess_time += post_time
                total_total_time += total_time
                image_count += 1
            elif os.path.splitext(file_path)[-1].lower() in ['.mp4', '.avi', '.mov']:
                process_video(model, device, os.path.join(file_path, file_name), output_path, args.thrh)
        
        # 输出文件夹处理统计
        if image_count > 0:
            avg_preprocess = total_preprocess_time / image_count
            avg_inference = total_inference_time / image_count
            avg_postprocess = total_postprocess_time / image_count
            avg_total = total_total_time / image_count
            
            print(f"\n{'='*60}")
            print(f"Folder Processing Complete - Total Images: {image_count}")
            print(f"\nAverage Times per Image:")
            print(f"  Preprocessing: {avg_preprocess*1000:.2f} ms")
            print(f"  Inference:     {avg_inference*1000:.2f} ms")
            print(f"  Postprocessing:{avg_postprocess*1000:.2f} ms")
            print(f"  Total:         {avg_total*1000:.2f} ms ({1/avg_total:.2f} FPS)")
            print(f"\nTotal Processing Time: {total_total_time:.2f} seconds")
            print(f"{'='*60}")
    elif os.path.splitext(file_path)[-1].lower() in ['.jpg', '.jpeg', '.png', '.bmp']:
        # Process as single image
        process_image(model, device, file_path, output_path, args.thrh)
        logger.info("Image processing complete.")
    elif os.path.splitext(file_path)[-1].lower() in ['.mp4', '.avi', '.mov']:
        # Process as video
        process_video(model, device, file_path, output_path, args.thrh)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str,
                        default='D:/YOLO/DEIM/DEIM_20251224/DEIM/deim_outputs/deim_hgnetv2_n_test/best_stg2.engine')
    parser.add_argument('-i', '--input', type=str,
                        default='D:/YOLO/yolo-utils/dataset/weldArea/YOLO_Format/images/val')
    parser.add_argument('-o', '--output', type=str, default='D:/YOLO/DEIM/DEIM_20251224/DEIM/deim_outputs/inference_results/exp')
    parser.add_argument('-t', '--thrh', type=float, default=0.1)
    parser.add_argument('-d', '--device', type=str, default='cuda:0')
    args = parser.parse_args()
    main(args)