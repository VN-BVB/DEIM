
import torch

if __name__ == '__main__':
    weight = torch.load(r'D:\YOLO\DEIM\DEIM_20251224\DEIM\weight\hgnetv2/deim_dfine_hgnetv2_n_coco_160e.pth')
    old = weight.keys()

    new_weight = {}
    for keys in weight.keys():
        old_keys = keys
        if keys.startswith('stem.'):
            keys = keys.replace('stem.', '0.')
        elif keys.startswith('stages.0'):
            keys = keys.replace('stages.0', '1')
        elif keys.startswith('stages.1'):
            keys = keys.replace('stages.1', '2')
        elif keys.startswith('stages.2'):
            keys = keys.replace('stages.2', '3')
        elif keys.startswith('stages.3'):
            keys = keys.replace('stages.3', '4')
        
        new_weight[keys] = weight[old_keys]

    torch.save(new_weight, r'D:\YOLO\DEIM\DEIM_20251224\DEIM\weight\hgnetv2/deim_dfine_hgnetv2_n_coco_160e_MG.pth')