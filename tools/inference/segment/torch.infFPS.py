"""
D-FINE / DEIM inference + FPS benchmark
Engineering-level fair comparison with YOLO
"""

import os
import time
import torch
import torch.nn as nn
import torchvision.transforms as T
import numpy as np
from PIL import Image
import tqdm
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from engine.core import YAMLConfig
from engine.extre_module.utils import increment_path
from engine.logger_module import get_logger
from tools.inference.utils import draw

logger = get_logger(__name__)
CLASS_NAME = None


# =========================
# CUDA-safe timing
# =========================
def sync_time():
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    return time.time()


# =========================
# Model wrapper
# =========================
class DeployModel(nn.Module):
    def __init__(self, cfg, state_dict):
        super().__init__()
        cfg.model.load_state_dict(state_dict)
        self.model = cfg.model.deploy()
        self.postprocessor = cfg.postprocessor.deploy()

    def forward(self, images, orig_target_sizes):
        outputs = self.model(images)
        outputs = self.postprocessor(outputs, orig_target_sizes)
        return outputs


# =========================
# Image processing with FPS
# =========================
def process_image(model, device, img_path, output_dir, thrh, timer):
    # ---------- Preprocess ----------
    t0 = sync_time()

    im = Image.open(img_path).convert("RGB")
    w, h = im.size
    orig_size = torch.tensor([[w, h]], device=device)

    transform = T.Compose([
        T.Resize((640, 640)),
        T.ToTensor()
    ])
    img_tensor = transform(im).unsqueeze(0).to(device)

    t1 = sync_time()

    # ---------- Inference ----------
    labels, boxes, scores, masks = model(img_tensor, orig_size)

    t2 = sync_time()

    # ---------- Postprocess ----------
    im = draw(
        [im],
        labels,
        boxes,
        scores,
        masks=masks,
        thrh=thrh,
        class_name=CLASS_NAME
    )
    im.save(output_dir / os.path.basename(img_path))

    t3 = sync_time()

    # ---------- Accumulate ----------
    timer["pre"]  += (t1 - t0)
    timer["inf"]  += (t2 - t1)
    timer["post"] += (t3 - t2)
    timer["num"]  += 1


# =========================
# Main
# =========================
def main(args):
    global CLASS_NAME

    cfg = YAMLConfig(args.config, resume=args.resume)

    if 'HGNetv2' in cfg.yaml_cfg:
        cfg.yaml_cfg['HGNetv2']['pretrained'] = False

    checkpoint = torch.load(args.resume, map_location='cpu')
    CLASS_NAME = checkpoint.get("name", None)

    state = checkpoint['ema']['module'] if 'ema' in checkpoint else checkpoint['model']

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = DeployModel(cfg, state).to(device)
    model.eval()

    output_dir = increment_path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # ---------- Timer ----------
    timer = {
        "pre": 0.0,
        "inf": 0.0,
        "post": 0.0,
        "num": 0
    }

    img_dir = args.input
    img_list = [
        f for f in os.listdir(img_dir)
        if f.lower().endswith(('.jpg', '.png', '.bmp'))
    ]

    for name in tqdm.tqdm(img_list, desc="Running inference"):
        process_image(
            model,
            device,
            os.path.join(img_dir, name),
            output_dir,
            args.thrh,
            timer
        )

    # ---------- Report ----------
    if timer["num"] > 0:
        pre_ms  = timer["pre"]  / timer["num"] * 1000
        inf_ms  = timer["inf"]  / timer["num"] * 1000
        # post_ms = timer["post"] / timer["num"] * 1000
        total_ms = pre_ms + inf_ms # + post_ms

        print("\n================ FPS Benchmark (D-FINE) ================")
        print("Average Times per Image:")
        print(f"Preprocessing:  {pre_ms:.2f} ms")
        print(f"Inference:      {inf_ms:.2f} ms")
        # print(f"Postprocessing:{post_ms:.2f} ms")
        print(f"Total:          {total_ms:.2f} ms ({1000 / total_ms:.2f} FPS)")
        print("========================================================")


# =========================
# CLI
# =========================
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--config",
        default=r"D:\YOLO\DEIM\DEIM_20251224\DEIM\configs\seg\define-s-seg_MG.yml"
    )
    parser.add_argument(
        "-r", "--resume",
        default=r"weight\seg\define-s-seg.pth"
    )
    parser.add_argument(
        "-i", "--input",
        default=r"D:\YOLO\dataset\3EAweldArea\maskWeld\VOC\JPEGImages"
    )
    parser.add_argument(
        "-o", "--output",
        default="D:/YOLO/DEIM/DEIM_20251224/DEIM/inference_results/exp"
    )
    parser.add_argument("-t", "--thrh", type=float, default=0.2)

    args = parser.parse_args()
    main(args)
