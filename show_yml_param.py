import json, argparse
from engine.core import YAMLConfig

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '-c', default= "D:\YOLO\DEIM\DEIM_20251224\DEIM\configs\yaml\dfine_hgnetv2_n_mg.yml", type=str)
    args = parser.parse_args()

    cfg = YAMLConfig(args.config, resume=None)
    print(json.dumps(cfg.__dict__, indent=4, ensure_ascii=False))