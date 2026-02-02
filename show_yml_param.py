import json, argparse
from engine.core import YAMLConfig

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '-c', default= "D:\YOLO\DEIM\DEIM_20251224\DEIM\configs\seg\define-n-seg.yml", type=str)
    args = parser.parse_args()

    cfg = YAMLConfig(args.config, resume=None)
    print(json.dumps(cfg.__dict__, indent=4, ensure_ascii=False))