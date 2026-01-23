D:\anaconda\envs\yolov11\python.exe D:\YOLO\DEIM\DEIM_20251224\DEIM\train.py 
Not init distributed mode.
PyTorch 版本: 2.8.0+cu126
Torchvision 版本: 0.23.0+cu126
CUDA 是否可用: True
GPU 数量: 1
GPU 0: NVIDIA GeForce RTX 4060 Laptop GPU
  显存: 8.00 GB
  计算能力: (8, 9)
当前设备索引: 0
当前设备名称: NVIDIA GeForce RTX 4060 Laptop GPU
{
    "task": "detection",
    "_model": null,
    "_postprocessor": null,
    "_criterion": null,
    "_optimizer": null,
    "_lr_scheduler": null,
    "_lr_warmup_scheduler": null,
    "_train_dataloader": null,
    "_val_dataloader": null,
    "_ema": null,
    "_scaler": null,
    "_train_dataset": null,
    "_val_dataset": null,
    "_collate_fn": null,
    "_evaluator": null,
    "_writer": null,
    "num_workers": 0,
    "batch_size": null,
    "_train_batch_size": null,
    "_val_batch_size": null,
    "_train_shuffle": null,
    "_val_shuffle": null,
    "resume": null,
    "tuning": "D:\\YOLO\\DEIM\\DEIM_20251224\\DEIM\\weight\\hgnetv2\\deim_dfine_hgnetv2_n_coco_160e_MG.pth",
    "path": null,
    "epoches": 400,
    "last_epoch": -1,
    "lrsheduler": "flatcosine",
    "lr_gamma": 0.8,
    "no_aug_epoch": 20,
    "warmup_iter": 2000,
    "flat_epoch": 194,
    "use_amp": false,
    "use_ema": true,
    "ema_decay": 0.9999,
    "ema_warmups": 2000,
    "sync_bn": true,
    "clip_max_norm": 0.1,
    "find_unused_parameters": true,
    "seed": 0,
    "print_freq": 50,
    "checkpoint_freq": 50,
    "plot_train_batch_freq": 50,
    "output_dir": "./outputs/deim_hgnetv2_n_custom",
    "summary_dir": null,
    "device": "",
    "verbose_type": "progress",
    "cache_imgsz": 640,
    "ram_cache": true,
    "yolo_metrice": true,
    "prune_model": false,
    "kd_loss_type": null,
    "kd_loss_decay": null,
    "kd_loss_epoch": 1.0,
    "logical_loss_type": "single",
    "logical_loss_ratio": 1.0,
    "teacher_kd_layers": null,
    "student_kd_layers": null,
    "feature_loss_type": "cwd",
    "feature_loss_ratio": 1.0,
    "yaml_cfg": {
        "task": "detection",
        "evaluator": {
            "type": "CocoEvaluator",
            "iou_types": [
                "bbox"
            ]
        },
        "num_classes": 7,
        "remap_mscoco_category": false,
        "train_dataloader": {
            "type": "DataLoader",
            "dataset": {
                "type": "CocoDetection",
                "img_folder": "D:/YOLO/dataset/RomWeldArea/images",
                "ann_file": "D:/YOLO/dataset/RomWeldArea/annotations/train.json",
                "return_masks": false,
                "transforms": {
                    "type": "Compose",
                    "ops": [
                        {
                            "type": "Mosaic",
                            "output_size": 320,
                            "rotation_range": 10,
                            "translation_range": [
                                0.1,
                                0.1
                            ],
                            "scaling_range": [
                                0.5,
                                1.5
                            ],
                            "probability": 1.0,
                            "fill_value": 0,
                            "use_cache": false,
                            "max_cached_images": 50,
                            "random_pop": true
                        },
                        {
                            "type": "RandomPhotometricDistort",
                            "p": 0.5
                        },
                        {
                            "type": "RandomZoomOut",
                            "fill": 0
                        },
                        {
                            "type": "RandomIoUCrop",
                            "p": 0.8
                        },
                        {
                            "type": "SanitizeBoundingBoxes",
                            "min_size": 1
                        },
                        {
                            "type": "RandomHorizontalFlip"
                        },
                        {
                            "type": "Resize",
                            "size": [
                                640,
                                640
                            ]
                        },
                        {
                            "type": "SanitizeBoundingBoxes",
                            "min_size": 1
                        },
                        {
                            "type": "ConvertPILImage",
                            "dtype": "float32",
                            "scale": true
                        },
                        {
                            "type": "ConvertBoxes",
                            "fmt": "cxcywh",
                            "normalize": true
                        }
                    ],
                    "policy": {
                        "name": "stop_epoch",
                        "epoch": [
                            4,
                            194,
                            380
                        ],
                        "ops": [
                            "Mosaic",
                            "RandomPhotometricDistort",
                            "RandomZoomOut",
                            "RandomIoUCrop"
                        ]
                    },
                    "mosaic_prob": 0.5
                }
            },
            "shuffle": true,
            "num_workers": 16,
            "drop_last": true,
            "pin_memory": true,
            "collate_fn": {
                "type": "BatchImageCollateFunction",
                "base_size": 640,
                "base_size_repeat": null,
                "stop_epoch": 380,
                "ema_restart_decay": 0.9999,
                "mixup_prob": 0.4,
                "mixup_epochs": [
                    4,
                    194
                ]
            },
            "total_batch_size": 8
        },
        "val_dataloader": {
            "type": "DataLoader",
            "dataset": {
                "type": "CocoDetection",
                "img_folder": "D:/YOLO/dataset/RomWeldArea/images",
                "ann_file": "D:/YOLO/dataset/RomWeldArea/annotations/val.json",
                "return_masks": false,
                "transforms": {
                    "type": "Compose",
                    "ops": [
                        {
                            "type": "Resize",
                            "size": [
                                640,
                                640
                            ]
                        },
                        {
                            "type": "ConvertPILImage",
                            "dtype": "float32",
                            "scale": true
                        }
                    ]
                }
            },
            "shuffle": false,
            "num_workers": 4,
            "drop_last": false,
            "pin_memory": true,
            "collate_fn": {
                "type": "BatchImageCollateFunction"
            },
            "total_batch_size": 8
        },
        "print_freq": 50,
        "output_dir": "./outputs/deim_hgnetv2_n_custom",
        "checkpoint_freq": 50,
        "plot_train_batch_freq": 50,
        "sync_bn": true,
        "find_unused_parameters": true,
        "verbose_type": "progress",
        "use_amp": false,
        "scaler": {
            "type": "GradScaler",
            "enabled": true
        },
        "use_ema": true,
        "ema": {
            "type": "ModelEMA",
            "decay": 0.9999,
            "warmups": 1000,
            "start": 0
        },
        "cache_imgsz": 640,
        "ram_cache": true,
        "yolo_metrice": true,
        "epoches": 400,
        "clip_max_norm": 0.1,
        "optimizer": {
            "type": "AdamW",
            "params": [
                {
                    "params": "^(?=.*backbone)(?!.*norm|bn).*$",
                    "lr": 0.0004
                },
                {
                    "params": "^(?=.*backbone)(?=.*norm|bn).*$",
                    "lr": 0.0004,
                    "weight_decay": 0.0
                },
                {
                    "params": "^(?=.*(?:encoder|decoder))(?=.*(?:norm|bn|bias)).*$",
                    "weight_decay": 0.0
                }
            ],
            "lr": 0.0008,
            "betas": [
                0.9,
                0.999
            ],
            "weight_decay": 0.0001
        },
        "lr_scheduler": {
            "type": "MultiStepLR",
            "milestones": [
                500
            ],
            "gamma": 0.1
        },
        "lr_warmup_scheduler": {
            "type": "LinearWarmup",
            "warmup_duration": 500
        },
        "model": "DEIM_MG",
        "criterion": "DEIMCriterion",
        "postprocessor": "PostProcessor",
        "use_focal_loss": true,
        "eval_spatial_size": [
            640,
            640
        ],
        "DEIM": {
            "backbone": "HGNetv2",
            "encoder": "HybridEncoder",
            "decoder": "DFINETransformer"
        },
        "lrsheduler": "flatcosine",
        "lr_gamma": 0.8,
        "warmup_iter": 2000,
        "flat_epoch": 194,
        "no_aug_epoch": 20,
        "HGNetv2": {
            "pretrained": false,
            "local_model_dir": "./weight/hgnetv2/",
            "name": "B0",
            "return_idx": [
                2,
                3
            ],
            "freeze_at": -1,
            "freeze_norm": false,
            "use_lab": true
        },
        "HybridEncoder": {
            "in_channels": [
                512,
                1024
            ],
            "feat_strides": [
                16,
                32
            ],
            "hidden_dim": 128,
            "use_encoder_idx": [
                1
            ],
            "num_encoder_layers": 1,
            "nhead": 8,
            "dim_feedforward": 512,
            "dropout": 0.0,
            "enc_act": "gelu",
            "expansion": 0.34,
            "depth_mult": 0.5,
            "act": "silu"
        },
        "DFINETransformer": {
            "feat_channels": [
                128,
                128
            ],
            "feat_strides": [
                16,
                32
            ],
            "hidden_dim": 128,
            "num_levels": 2,
            "num_layers": 3,
            "eval_idx": -1,
            "num_queries": 300,
            "num_denoising": 100,
            "label_noise_ratio": 0.5,
            "box_noise_scale": 1.0,
            "reg_max": 32,
            "reg_scale": 4,
            "layer_scale": 1,
            "num_points": [
                6,
                6
            ],
            "cross_attn_method": "default",
            "query_select_method": "default",
            "dim_feedforward": 512,
            "activation": "silu",
            "mlp_act": "silu"
        },
        "PostProcessor": {
            "num_top_queries": 300
        },
        "DEIMCriterion": {
            "weight_dict": {
                "loss_vfl": 1,
                "loss_bbox": 5,
                "loss_giou": 2,
                "loss_fgl": 0.15,
                "loss_ddf": 1.5,
                "loss_mal": 1
            },
            "losses": [
                "mal",
                "boxes",
                "local"
            ],
            "alpha": 0.75,
            "gamma": 1.5,
            "reg_max": 32,
            "matcher": {
                "type": "HungarianMatcher",
                "weight_dict": {
                    "cost_class": 2,
                    "cost_bbox": 5,
                    "cost_giou": 2
                },
                "alpha": 0.25,
                "gamma": 2.0
            }
        },
        "__include__": [
            "../dfine/dfine_hgnetv2_n_custom.yml",
            "../dataset/user_detection.yml",
            "../base/deim.yml"
        ],
        "DEIM_MG": {
            "yaml_path": "configs/cfg/dfine-n.yaml"
        },
        "config": "D:\\YOLO\\DEIM\\DEIM_20251224\\DEIM\\configs\\yaml\\user_deim_dfine_hgnetv2_n_mg.yml",
        "tuning": "D:\\YOLO\\DEIM\\DEIM_20251224\\DEIM\\weight\\hgnetv2\\deim_dfine_hgnetv2_n_coco_160e_MG.pth",
        "seed": 0,
        "test_only": false,
        "mode": "det",
        "print_method": "builtin",
        "print_rank": 0
    }
}
2026-01-20 15:38:47 [tasks.py:parse_model:302] INFO:          from    params  module                                                      arguments                     
2026-01-20 15:38:47 [tasks.py:parse_model:307] INFO: ----------------------------------------BackBone----------------------------------------
2026-01-20 15:38:47 [tasks.py:parse_model:313] INFO:   0        -1      6474  engine.backbone.hgnetv2.StemBlock                           [3, 16, 16, True]             
2026-01-20 15:38:47 [tasks.py:parse_model:313] INFO:   1        -1     11306  engine.backbone.hgnetv2.HG_Stage                            [16, 16, 64, 1, 3, False, False, 3, True, 'se']
2026-01-20 15:38:47 [tasks.py:parse_model:313] INFO:   2        -1     91786  engine.backbone.hgnetv2.HG_Stage                            [64, 32, 256, 1, 3, True, False, 3, True, 'se']
2026-01-20 15:38:47 [tasks.py:parse_model:313] INFO:   3        -1    639636  engine.backbone.hgnetv2.HG_Stage                            [256, 64, 512, 2, 3, True, True, 5, True, 'se']
2026-01-20 15:38:47 [tasks.py:parse_model:313] INFO:   4        -1   1101194  engine.backbone.hgnetv2.HG_Stage                            [512, 128, 1024, 1, 3, True, True, 5, True, 'se']
2026-01-20 15:38:47 [tasks.py:parse_model:324] INFO: ----------------------------------------Enchoder----------------------------------------
2026-01-20 15:38:47 [tasks.py:parse_model:330] INFO:   5         3     65792  engine.deim.hybrid_encoder.ConvNormLayer_fuse               [512, 128, 1, 1]              
2026-01-20 15:38:47 [tasks.py:parse_model:330] INFO:   6         4    131328  engine.deim.hybrid_encoder.ConvNormLayer_fuse               [1024, 128, 1, 1]             
2026-01-20 15:38:47 [tasks.py:parse_model:330] INFO:   7        -1    198272  engine.deim.hybrid_encoder.TransformerEncoderBlock          [128, 8, 512, 0.1, 'relu', 10000, False]
2026-01-20 15:38:47 [tasks.py:parse_model:330] INFO:   8        -1     16640  engine.deim.hybrid_encoder.ConvNormLayer_fuse               [128, 128, 1, 1]              
2026-01-20 15:38:47 [tasks.py:parse_model:330] INFO:   9        -1         0  torch.nn.modules.upsampling.Upsample                        [None, 2, 'nearest']          
2026-01-20 15:38:47 [tasks.py:parse_model:330] INFO:  10   [-1, 5]         0  engine.extre_module.ultralytics_nn.conv.Concat              []                            
2026-01-20 15:38:47 [tasks.py:parse_model:330] INFO:  11        -1    136872  engine.deim.hybrid_encoder.RepNCSPELAN4                     [256, 128, 256, 21, 2, False, 'silu']
2026-01-20 15:38:47 [tasks.py:parse_model:330] INFO:  12        -1     18048  engine.deim.hybrid_encoder.SCDown                           [128, 128, 3, 2, 'silu']      
2026-01-20 15:38:47 [tasks.py:parse_model:330] INFO:  13   [-1, 8]         0  engine.extre_module.ultralytics_nn.conv.Concat              []                            
2026-01-20 15:38:47 [tasks.py:parse_model:330] INFO:  14        -1    136872  engine.deim.hybrid_encoder.RepNCSPELAN4                     [256, 128, 256, 21, 2, False, 'silu']
2026-01-20 15:38:47 [tasks.py:parse_model:339] INFO: ----------------------------------------Decoder----------------------------------------
2026-01-20 15:38:47 [tasks.py:parse_model:345] INFO:  15  [11, 14]   1181461  engine.deim.dfine_decoder.DFINETransformer                  {'feat_strides': [16, 32], 'hidden_dim': 128, 'num_levels': 2, 'num_layers': 3, 'num_points': [6, 6], 'dim_feedforward': 512, 'feat_channels': [128, 128], 'num_classes': 7, 'eval_spatial_size': [640, 640]}
2026-01-20 15:38:47 [_solver.py:_setup:72] INFO: Tuning checkpoint from D:\YOLO\DEIM\DEIM_20251224\DEIM\weight\hgnetv2\deim_dfine_hgnetv2_n_coco_160e_MG.pth
2026-01-20 15:38:47 [_solver.py:load_tuning_state:232] INFO: Load model.state_dict, {'missed': ['backbone.0.stem1.conv.weight', 'backbone.0.stem1.bn.weight', 'backbone.0.stem1.bn.bias', 'backbone.0.stem1.bn.running_mean', 'backbone.0.stem1.bn.running_var', 'backbone.0.stem1.bn.num_batches_tracked', 'backbone.0.stem1.lab.scale', 'backbone.0.stem1.lab.bias', 'backbone.0.stem2a.conv.weight', 'backbone.0.stem2a.bn.weight', 'backbone.0.stem2a.bn.bias', 'backbone.0.stem2a.bn.running_mean', 'backbone.0.stem2a.bn.running_var', 'backbone.0.stem2a.bn.num_batches_tracked', 'backbone.0.stem2a.lab.scale', 'backbone.0.stem2a.lab.bias', 'backbone.0.stem2b.conv.weight', 'backbone.0.stem2b.bn.weight', 'backbone.0.stem2b.bn.bias', 'backbone.0.stem2b.bn.running_mean', 'backbone.0.stem2b.bn.running_var', 'backbone.0.stem2b.bn.num_batches_tracked', 'backbone.0.stem2b.lab.scale', 'backbone.0.stem2b.lab.bias', 'backbone.0.stem3.conv.weight', 'backbone.0.stem3.bn.weight', 'backbone.0.stem3.bn.bias', 'backbone.0.stem3.bn.running_mean', 'backbone.0.stem3.bn.running_var', 'backbone.0.stem3.bn.num_batches_tracked', 'backbone.0.stem3.lab.scale', 'backbone.0.stem3.lab.bias', 'backbone.0.stem4.conv.weight', 'backbone.0.stem4.bn.weight', 'backbone.0.stem4.bn.bias', 'backbone.0.stem4.bn.running_mean', 'backbone.0.stem4.bn.running_var', 'backbone.0.stem4.bn.num_batches_tracked', 'backbone.0.stem4.lab.scale', 'backbone.0.stem4.lab.bias', 'backbone.1.blocks.0.layers.0.conv.weight', 'backbone.1.blocks.0.layers.0.bn.weight', 'backbone.1.blocks.0.layers.0.bn.bias', 'backbone.1.blocks.0.layers.0.bn.running_mean', 'backbone.1.blocks.0.layers.0.bn.running_var', 'backbone.1.blocks.0.layers.0.bn.num_batches_tracked', 'backbone.1.blocks.0.layers.0.lab.scale', 'backbone.1.blocks.0.layers.0.lab.bias', 'backbone.1.blocks.0.layers.1.conv.weight', 'backbone.1.blocks.0.layers.1.bn.weight', 'backbone.1.blocks.0.layers.1.bn.bias', 'backbone.1.blocks.0.layers.1.bn.running_mean', 'backbone.1.blocks.0.layers.1.bn.running_var', 'backbone.1.blocks.0.layers.1.bn.num_batches_tracked', 'backbone.1.blocks.0.layers.1.lab.scale', 'backbone.1.blocks.0.layers.1.lab.bias', 'backbone.1.blocks.0.layers.2.conv.weight', 'backbone.1.blocks.0.layers.2.bn.weight', 'backbone.1.blocks.0.layers.2.bn.bias', 'backbone.1.blocks.0.layers.2.bn.running_mean', 'backbone.1.blocks.0.layers.2.bn.running_var', 'backbone.1.blocks.0.layers.2.bn.num_batches_tracked', 'backbone.1.blocks.0.layers.2.lab.scale', 'backbone.1.blocks.0.layers.2.lab.bias', 'backbone.1.blocks.0.aggregation.0.conv.weight', 'backbone.1.blocks.0.aggregation.0.bn.weight', 'backbone.1.blocks.0.aggregation.0.bn.bias', 'backbone.1.blocks.0.aggregation.0.bn.running_mean', 'backbone.1.blocks.0.aggregation.0.bn.running_var', 'backbone.1.blocks.0.aggregation.0.bn.num_batches_tracked', 'backbone.1.blocks.0.aggregation.0.lab.scale', 'backbone.1.blocks.0.aggregation.0.lab.bias', 'backbone.1.blocks.0.aggregation.1.conv.weight', 'backbone.1.blocks.0.aggregation.1.bn.weight', 'backbone.1.blocks.0.aggregation.1.bn.bias', 'backbone.1.blocks.0.aggregation.1.bn.running_mean', 'backbone.1.blocks.0.aggregation.1.bn.running_var', 'backbone.1.blocks.0.aggregation.1.bn.num_batches_tracked', 'backbone.1.blocks.0.aggregation.1.lab.scale', 'backbone.1.blocks.0.aggregation.1.lab.bias', 'backbone.2.downsample.conv.weight', 'backbone.2.downsample.bn.weight', 'backbone.2.downsample.bn.bias', 'backbone.2.downsample.bn.running_mean', 'backbone.2.downsample.bn.running_var', 'backbone.2.downsample.bn.num_batches_tracked', 'backbone.2.blocks.0.layers.0.conv.weight', 'backbone.2.blocks.0.layers.0.bn.weight', 'backbone.2.blocks.0.layers.0.bn.bias', 'backbone.2.blocks.0.layers.0.bn.running_mean', 'backbone.2.blocks.0.layers.0.bn.running_var', 'backbone.2.blocks.0.layers.0.bn.num_batches_tracked', 'backbone.2.blocks.0.layers.0.lab.scale', 'backbone.2.blocks.0.layers.0.lab.bias', 'backbone.2.blocks.0.layers.1.conv.weight', 'backbone.2.blocks.0.layers.1.bn.weight', 'backbone.2.blocks.0.layers.1.bn.bias', 'backbone.2.blocks.0.layers.1.bn.running_mean', 'backbone.2.blocks.0.layers.1.bn.running_var', 'backbone.2.blocks.0.layers.1.bn.num_batches_tracked', 'backbone.2.blocks.0.layers.1.lab.scale', 'backbone.2.blocks.0.layers.1.lab.bias', 'backbone.2.blocks.0.layers.2.conv.weight', 'backbone.2.blocks.0.layers.2.bn.weight', 'backbone.2.blocks.0.layers.2.bn.bias', 'backbone.2.blocks.0.layers.2.bn.running_mean', 'backbone.2.blocks.0.layers.2.bn.running_var', 'backbone.2.blocks.0.layers.2.bn.num_batches_tracked', 'backbone.2.blocks.0.layers.2.lab.scale', 'backbone.2.blocks.0.layers.2.lab.bias', 'backbone.2.blocks.0.aggregation.0.conv.weight', 'backbone.2.blocks.0.aggregation.0.bn.weight', 'backbone.2.blocks.0.aggregation.0.bn.bias', 'backbone.2.blocks.0.aggregation.0.bn.running_mean', 'backbone.2.blocks.0.aggregation.0.bn.running_var', 'backbone.2.blocks.0.aggregation.0.bn.num_batches_tracked', 'backbone.2.blocks.0.aggregation.0.lab.scale', 'backbone.2.blocks.0.aggregation.0.lab.bias', 'backbone.2.blocks.0.aggregation.1.conv.weight', 'backbone.2.blocks.0.aggregation.1.bn.weight', 'backbone.2.blocks.0.aggregation.1.bn.bias', 'backbone.2.blocks.0.aggregation.1.bn.running_mean', 'backbone.2.blocks.0.aggregation.1.bn.running_var', 'backbone.2.blocks.0.aggregation.1.bn.num_batches_tracked', 'backbone.2.blocks.0.aggregation.1.lab.scale', 'backbone.2.blocks.0.aggregation.1.lab.bias', 'backbone.3.downsample.conv.weight', 'backbone.3.downsample.bn.weight', 'backbone.3.downsample.bn.bias', 'backbone.3.downsample.bn.running_mean', 'backbone.3.downsample.bn.running_var', 'backbone.3.downsample.bn.num_batches_tracked', 'backbone.3.blocks.0.layers.0.conv1.conv.weight', 'backbone.3.blocks.0.layers.0.conv1.bn.weight', 'backbone.3.blocks.0.layers.0.conv1.bn.bias', 'backbone.3.blocks.0.layers.0.conv1.bn.running_mean', 'backbone.3.blocks.0.layers.0.conv1.bn.running_var', 'backbone.3.blocks.0.layers.0.conv1.bn.num_batches_tracked', 'backbone.3.blocks.0.layers.0.conv2.conv.weight', 'backbone.3.blocks.0.layers.0.conv2.bn.weight', 'backbone.3.blocks.0.layers.0.conv2.bn.bias', 'backbone.3.blocks.0.layers.0.conv2.bn.running_mean', 'backbone.3.blocks.0.layers.0.conv2.bn.running_var', 'backbone.3.blocks.0.layers.0.conv2.bn.num_batches_tracked', 'backbone.3.blocks.0.layers.0.conv2.lab.scale', 'backbone.3.blocks.0.layers.0.conv2.lab.bias', 'backbone.3.blocks.0.layers.1.conv1.conv.weight', 'backbone.3.blocks.0.layers.1.conv1.bn.weight', 'backbone.3.blocks.0.layers.1.conv1.bn.bias', 'backbone.3.blocks.0.layers.1.conv1.bn.running_mean', 'backbone.3.blocks.0.layers.1.conv1.bn.running_var', 'backbone.3.blocks.0.layers.1.conv1.bn.num_batches_tracked', 'backbone.3.blocks.0.layers.1.conv2.conv.weight', 'backbone.3.blocks.0.layers.1.conv2.bn.weight', 'backbone.3.blocks.0.layers.1.conv2.bn.bias', 'backbone.3.blocks.0.layers.1.conv2.bn.running_mean', 'backbone.3.blocks.0.layers.1.conv2.bn.running_var', 'backbone.3.blocks.0.layers.1.conv2.bn.num_batches_tracked', 'backbone.3.blocks.0.layers.1.conv2.lab.scale', 'backbone.3.blocks.0.layers.1.conv2.lab.bias', 'backbone.3.blocks.0.layers.2.conv1.conv.weight', 'backbone.3.blocks.0.layers.2.conv1.bn.weight', 'backbone.3.blocks.0.layers.2.conv1.bn.bias', 'backbone.3.blocks.0.layers.2.conv1.bn.running_mean', 'backbone.3.blocks.0.layers.2.conv1.bn.running_var', 'backbone.3.blocks.0.layers.2.conv1.bn.num_batches_tracked', 'backbone.3.blocks.0.layers.2.conv2.conv.weight', 'backbone.3.blocks.0.layers.2.conv2.bn.weight', 'backbone.3.blocks.0.layers.2.conv2.bn.bias', 'backbone.3.blocks.0.layers.2.conv2.bn.running_mean', 'backbone.3.blocks.0.layers.2.conv2.bn.running_var', 'backbone.3.blocks.0.layers.2.conv2.bn.num_batches_tracked', 'backbone.3.blocks.0.layers.2.conv2.lab.scale', 'backbone.3.blocks.0.layers.2.conv2.lab.bias', 'backbone.3.blocks.0.aggregation.0.conv.weight', 'backbone.3.blocks.0.aggregation.0.bn.weight', 'backbone.3.blocks.0.aggregation.0.bn.bias', 'backbone.3.blocks.0.aggregation.0.bn.running_mean', 'backbone.3.blocks.0.aggregation.0.bn.running_var', 'backbone.3.blocks.0.aggregation.0.bn.num_batches_tracked', 'backbone.3.blocks.0.aggregation.0.lab.scale', 'backbone.3.blocks.0.aggregation.0.lab.bias', 'backbone.3.blocks.0.aggregation.1.conv.weight', 'backbone.3.blocks.0.aggregation.1.bn.weight', 'backbone.3.blocks.0.aggregation.1.bn.bias', 'backbone.3.blocks.0.aggregation.1.bn.running_mean', 'backbone.3.blocks.0.aggregation.1.bn.running_var', 'backbone.3.blocks.0.aggregation.1.bn.num_batches_tracked', 'backbone.3.blocks.0.aggregation.1.lab.scale', 'backbone.3.blocks.0.aggregation.1.lab.bias', 'backbone.3.blocks.1.layers.0.conv1.conv.weight', 'backbone.3.blocks.1.layers.0.conv1.bn.weight', 'backbone.3.blocks.1.layers.0.conv1.bn.bias', 'backbone.3.blocks.1.layers.0.conv1.bn.running_mean', 'backbone.3.blocks.1.layers.0.conv1.bn.running_var', 'backbone.3.blocks.1.layers.0.conv1.bn.num_batches_tracked', 'backbone.3.blocks.1.layers.0.conv2.conv.weight', 'backbone.3.blocks.1.layers.0.conv2.bn.weight', 'backbone.3.blocks.1.layers.0.conv2.bn.bias', 'backbone.3.blocks.1.layers.0.conv2.bn.running_mean', 'backbone.3.blocks.1.layers.0.conv2.bn.running_var', 'backbone.3.blocks.1.layers.0.conv2.bn.num_batches_tracked', 'backbone.3.blocks.1.layers.0.conv2.lab.scale', 'backbone.3.blocks.1.layers.0.conv2.lab.bias', 'backbone.3.blocks.1.layers.1.conv1.conv.weight', 'backbone.3.blocks.1.layers.1.conv1.bn.weight', 'backbone.3.blocks.1.layers.1.conv1.bn.bias', 'backbone.3.blocks.1.layers.1.conv1.bn.running_mean', 'backbone.3.blocks.1.layers.1.conv1.bn.running_var', 'backbone.3.blocks.1.layers.1.conv1.bn.num_batches_tracked', 'backbone.3.blocks.1.layers.1.conv2.conv.weight', 'backbone.3.blocks.1.layers.1.conv2.bn.weight', 'backbone.3.blocks.1.layers.1.conv2.bn.bias', 'backbone.3.blocks.1.layers.1.conv2.bn.running_mean', 'backbone.3.blocks.1.layers.1.conv2.bn.running_var', 'backbone.3.blocks.1.layers.1.conv2.bn.num_batches_tracked', 'backbone.3.blocks.1.layers.1.conv2.lab.scale', 'backbone.3.blocks.1.layers.1.conv2.lab.bias', 'backbone.3.blocks.1.layers.2.conv1.conv.weight', 'backbone.3.blocks.1.layers.2.conv1.bn.weight', 'backbone.3.blocks.1.layers.2.conv1.bn.bias', 'backbone.3.blocks.1.layers.2.conv1.bn.running_mean', 'backbone.3.blocks.1.layers.2.conv1.bn.running_var', 'backbone.3.blocks.1.layers.2.conv1.bn.num_batches_tracked', 'backbone.3.blocks.1.layers.2.conv2.conv.weight', 'backbone.3.blocks.1.layers.2.conv2.bn.weight', 'backbone.3.blocks.1.layers.2.conv2.bn.bias', 'backbone.3.blocks.1.layers.2.conv2.bn.running_mean', 'backbone.3.blocks.1.layers.2.conv2.bn.running_var', 'backbone.3.blocks.1.layers.2.conv2.bn.num_batches_tracked', 'backbone.3.blocks.1.layers.2.conv2.lab.scale', 'backbone.3.blocks.1.layers.2.conv2.lab.bias', 'backbone.3.blocks.1.aggregation.0.conv.weight', 'backbone.3.blocks.1.aggregation.0.bn.weight', 'backbone.3.blocks.1.aggregation.0.bn.bias', 'backbone.3.blocks.1.aggregation.0.bn.running_mean', 'backbone.3.blocks.1.aggregation.0.bn.running_var', 'backbone.3.blocks.1.aggregation.0.bn.num_batches_tracked', 'backbone.3.blocks.1.aggregation.0.lab.scale', 'backbone.3.blocks.1.aggregation.0.lab.bias', 'backbone.3.blocks.1.aggregation.1.conv.weight', 'backbone.3.blocks.1.aggregation.1.bn.weight', 'backbone.3.blocks.1.aggregation.1.bn.bias', 'backbone.3.blocks.1.aggregation.1.bn.running_mean', 'backbone.3.blocks.1.aggregation.1.bn.running_var', 'backbone.3.blocks.1.aggregation.1.bn.num_batches_tracked', 'backbone.3.blocks.1.aggregation.1.lab.scale', 'backbone.3.blocks.1.aggregation.1.lab.bias', 'backbone.4.downsample.conv.weight', 'backbone.4.downsample.bn.weight', 'backbone.4.downsample.bn.bias', 'backbone.4.downsample.bn.running_mean', 'backbone.4.downsample.bn.running_var', 'backbone.4.downsample.bn.num_batches_tracked', 'backbone.4.blocks.0.layers.0.conv1.conv.weight', 'backbone.4.blocks.0.layers.0.conv1.bn.weight', 'backbone.4.blocks.0.layers.0.conv1.bn.bias', 'backbone.4.blocks.0.layers.0.conv1.bn.running_mean', 'backbone.4.blocks.0.layers.0.conv1.bn.running_var', 'backbone.4.blocks.0.layers.0.conv1.bn.num_batches_tracked', 'backbone.4.blocks.0.layers.0.conv2.conv.weight', 'backbone.4.blocks.0.layers.0.conv2.bn.weight', 'backbone.4.blocks.0.layers.0.conv2.bn.bias', 'backbone.4.blocks.0.layers.0.conv2.bn.running_mean', 'backbone.4.blocks.0.layers.0.conv2.bn.running_var', 'backbone.4.blocks.0.layers.0.conv2.bn.num_batches_tracked', 'backbone.4.blocks.0.layers.0.conv2.lab.scale', 'backbone.4.blocks.0.layers.0.conv2.lab.bias', 'backbone.4.blocks.0.layers.1.conv1.conv.weight', 'backbone.4.blocks.0.layers.1.conv1.bn.weight', 'backbone.4.blocks.0.layers.1.conv1.bn.bias', 'backbone.4.blocks.0.layers.1.conv1.bn.running_mean', 'backbone.4.blocks.0.layers.1.conv1.bn.running_var', 'backbone.4.blocks.0.layers.1.conv1.bn.num_batches_tracked', 'backbone.4.blocks.0.layers.1.conv2.conv.weight', 'backbone.4.blocks.0.layers.1.conv2.bn.weight', 'backbone.4.blocks.0.layers.1.conv2.bn.bias', 'backbone.4.blocks.0.layers.1.conv2.bn.running_mean', 'backbone.4.blocks.0.layers.1.conv2.bn.running_var', 'backbone.4.blocks.0.layers.1.conv2.bn.num_batches_tracked', 'backbone.4.blocks.0.layers.1.conv2.lab.scale', 'backbone.4.blocks.0.layers.1.conv2.lab.bias', 'backbone.4.blocks.0.layers.2.conv1.conv.weight', 'backbone.4.blocks.0.layers.2.conv1.bn.weight', 'backbone.4.blocks.0.layers.2.conv1.bn.bias', 'backbone.4.blocks.0.layers.2.conv1.bn.running_mean', 'backbone.4.blocks.0.layers.2.conv1.bn.running_var', 'backbone.4.blocks.0.layers.2.conv1.bn.num_batches_tracked', 'backbone.4.blocks.0.layers.2.conv2.conv.weight', 'backbone.4.blocks.0.layers.2.conv2.bn.weight', 'backbone.4.blocks.0.layers.2.conv2.bn.bias', 'backbone.4.blocks.0.layers.2.conv2.bn.running_mean', 'backbone.4.blocks.0.layers.2.conv2.bn.running_var', 'backbone.4.blocks.0.layers.2.conv2.bn.num_batches_tracked', 'backbone.4.blocks.0.layers.2.conv2.lab.scale', 'backbone.4.blocks.0.layers.2.conv2.lab.bias', 'backbone.4.blocks.0.aggregation.0.conv.weight', 'backbone.4.blocks.0.aggregation.0.bn.weight', 'backbone.4.blocks.0.aggregation.0.bn.bias', 'backbone.4.blocks.0.aggregation.0.bn.running_mean', 'backbone.4.blocks.0.aggregation.0.bn.running_var', 'backbone.4.blocks.0.aggregation.0.bn.num_batches_tracked', 'backbone.4.blocks.0.aggregation.0.lab.scale', 'backbone.4.blocks.0.aggregation.0.lab.bias', 'backbone.4.blocks.0.aggregation.1.conv.weight', 'backbone.4.blocks.0.aggregation.1.bn.weight', 'backbone.4.blocks.0.aggregation.1.bn.bias', 'backbone.4.blocks.0.aggregation.1.bn.running_mean', 'backbone.4.blocks.0.aggregation.1.bn.running_var', 'backbone.4.blocks.0.aggregation.1.bn.num_batches_tracked', 'backbone.4.blocks.0.aggregation.1.lab.scale', 'backbone.4.blocks.0.aggregation.1.lab.bias', 'encoder.0.conv.weight', 'encoder.0.norm.weight', 'encoder.0.norm.bias', 'encoder.0.norm.running_mean', 'encoder.0.norm.running_var', 'encoder.0.norm.num_batches_tracked', 'encoder.1.conv.weight', 'encoder.1.norm.weight', 'encoder.1.norm.bias', 'encoder.1.norm.running_mean', 'encoder.1.norm.running_var', 'encoder.1.norm.num_batches_tracked', 'encoder.2.self_attn.in_proj_weight', 'encoder.2.self_attn.in_proj_bias', 'encoder.2.self_attn.out_proj.weight', 'encoder.2.self_attn.out_proj.bias', 'encoder.2.linear1.weight', 'encoder.2.linear1.bias', 'encoder.2.linear2.weight', 'encoder.2.linear2.bias', 'encoder.2.norm1.weight', 'encoder.2.norm1.bias', 'encoder.2.norm2.weight', 'encoder.2.norm2.bias', 'encoder.3.conv.weight', 'encoder.3.norm.weight', 'encoder.3.norm.bias', 'encoder.3.norm.running_mean', 'encoder.3.norm.running_var', 'encoder.3.norm.num_batches_tracked', 'encoder.6.cv1.conv.weight', 'encoder.6.cv1.norm.weight', 'encoder.6.cv1.norm.bias', 'encoder.6.cv1.norm.running_mean', 'encoder.6.cv1.norm.running_var', 'encoder.6.cv1.norm.num_batches_tracked', 'encoder.6.cv2.0.conv1.conv.weight', 'encoder.6.cv2.0.conv1.norm.weight', 'encoder.6.cv2.0.conv1.norm.bias', 'encoder.6.cv2.0.conv1.norm.running_mean', 'encoder.6.cv2.0.conv1.norm.running_var', 'encoder.6.cv2.0.conv1.norm.num_batches_tracked', 'encoder.6.cv2.0.conv2.conv.weight', 'encoder.6.cv2.0.conv2.norm.weight', 'encoder.6.cv2.0.conv2.norm.bias', 'encoder.6.cv2.0.conv2.norm.running_mean', 'encoder.6.cv2.0.conv2.norm.running_var', 'encoder.6.cv2.0.conv2.norm.num_batches_tracked', 'encoder.6.cv2.0.bottlenecks.0.conv1.conv.weight', 'encoder.6.cv2.0.bottlenecks.0.conv1.norm.weight', 'encoder.6.cv2.0.bottlenecks.0.conv1.norm.bias', 'encoder.6.cv2.0.bottlenecks.0.conv1.norm.running_mean', 'encoder.6.cv2.0.bottlenecks.0.conv1.norm.running_var', 'encoder.6.cv2.0.bottlenecks.0.conv1.norm.num_batches_tracked', 'encoder.6.cv2.0.bottlenecks.0.conv2.conv.weight', 'encoder.6.cv2.0.bottlenecks.0.conv2.norm.weight', 'encoder.6.cv2.0.bottlenecks.0.conv2.norm.bias', 'encoder.6.cv2.0.bottlenecks.0.conv2.norm.running_mean', 'encoder.6.cv2.0.bottlenecks.0.conv2.norm.running_var', 'encoder.6.cv2.0.bottlenecks.0.conv2.norm.num_batches_tracked', 'encoder.6.cv2.0.bottlenecks.1.conv1.conv.weight', 'encoder.6.cv2.0.bottlenecks.1.conv1.norm.weight', 'encoder.6.cv2.0.bottlenecks.1.conv1.norm.bias', 'encoder.6.cv2.0.bottlenecks.1.conv1.norm.running_mean', 'encoder.6.cv2.0.bottlenecks.1.conv1.norm.running_var', 'encoder.6.cv2.0.bottlenecks.1.conv1.norm.num_batches_tracked', 'encoder.6.cv2.0.bottlenecks.1.conv2.conv.weight', 'encoder.6.cv2.0.bottlenecks.1.conv2.norm.weight', 'encoder.6.cv2.0.bottlenecks.1.conv2.norm.bias', 'encoder.6.cv2.0.bottlenecks.1.conv2.norm.running_mean', 'encoder.6.cv2.0.bottlenecks.1.conv2.norm.running_var', 'encoder.6.cv2.0.bottlenecks.1.conv2.norm.num_batches_tracked', 'encoder.6.cv2.1.conv.weight', 'encoder.6.cv2.1.norm.weight', 'encoder.6.cv2.1.norm.bias', 'encoder.6.cv2.1.norm.running_mean', 'encoder.6.cv2.1.norm.running_var', 'encoder.6.cv2.1.norm.num_batches_tracked', 'encoder.6.cv3.0.conv1.conv.weight', 'encoder.6.cv3.0.conv1.norm.weight', 'encoder.6.cv3.0.conv1.norm.bias', 'encoder.6.cv3.0.conv1.norm.running_mean', 'encoder.6.cv3.0.conv1.norm.running_var', 'encoder.6.cv3.0.conv1.norm.num_batches_tracked', 'encoder.6.cv3.0.conv2.conv.weight', 'encoder.6.cv3.0.conv2.norm.weight', 'encoder.6.cv3.0.conv2.norm.bias', 'encoder.6.cv3.0.conv2.norm.running_mean', 'encoder.6.cv3.0.conv2.norm.running_var', 'encoder.6.cv3.0.conv2.norm.num_batches_tracked', 'encoder.6.cv3.0.bottlenecks.0.conv1.conv.weight', 'encoder.6.cv3.0.bottlenecks.0.conv1.norm.weight', 'encoder.6.cv3.0.bottlenecks.0.conv1.norm.bias', 'encoder.6.cv3.0.bottlenecks.0.conv1.norm.running_mean', 'encoder.6.cv3.0.bottlenecks.0.conv1.norm.running_var', 'encoder.6.cv3.0.bottlenecks.0.conv1.norm.num_batches_tracked', 'encoder.6.cv3.0.bottlenecks.0.conv2.conv.weight', 'encoder.6.cv3.0.bottlenecks.0.conv2.norm.weight', 'encoder.6.cv3.0.bottlenecks.0.conv2.norm.bias', 'encoder.6.cv3.0.bottlenecks.0.conv2.norm.running_mean', 'encoder.6.cv3.0.bottlenecks.0.conv2.norm.running_var', 'encoder.6.cv3.0.bottlenecks.0.conv2.norm.num_batches_tracked', 'encoder.6.cv3.0.bottlenecks.1.conv1.conv.weight', 'encoder.6.cv3.0.bottlenecks.1.conv1.norm.weight', 'encoder.6.cv3.0.bottlenecks.1.conv1.norm.bias', 'encoder.6.cv3.0.bottlenecks.1.conv1.norm.running_mean', 'encoder.6.cv3.0.bottlenecks.1.conv1.norm.running_var', 'encoder.6.cv3.0.bottlenecks.1.conv1.norm.num_batches_tracked', 'encoder.6.cv3.0.bottlenecks.1.conv2.conv.weight', 'encoder.6.cv3.0.bottlenecks.1.conv2.norm.weight', 'encoder.6.cv3.0.bottlenecks.1.conv2.norm.bias', 'encoder.6.cv3.0.bottlenecks.1.conv2.norm.running_mean', 'encoder.6.cv3.0.bottlenecks.1.conv2.norm.running_var', 'encoder.6.cv3.0.bottlenecks.1.conv2.norm.num_batches_tracked', 'encoder.6.cv3.1.conv.weight', 'encoder.6.cv3.1.norm.weight', 'encoder.6.cv3.1.norm.bias', 'encoder.6.cv3.1.norm.running_mean', 'encoder.6.cv3.1.norm.running_var', 'encoder.6.cv3.1.norm.num_batches_tracked', 'encoder.6.cv4.conv.weight', 'encoder.6.cv4.norm.weight', 'encoder.6.cv4.norm.bias', 'encoder.6.cv4.norm.running_mean', 'encoder.6.cv4.norm.running_var', 'encoder.6.cv4.norm.num_batches_tracked', 'encoder.7.cv1.conv.weight', 'encoder.7.cv1.norm.weight', 'encoder.7.cv1.norm.bias', 'encoder.7.cv1.norm.running_mean', 'encoder.7.cv1.norm.running_var', 'encoder.7.cv1.norm.num_batches_tracked', 'encoder.7.cv2.conv.weight', 'encoder.7.cv2.norm.weight', 'encoder.7.cv2.norm.bias', 'encoder.7.cv2.norm.running_mean', 'encoder.7.cv2.norm.running_var', 'encoder.7.cv2.norm.num_batches_tracked', 'encoder.9.cv1.conv.weight', 'encoder.9.cv1.norm.weight', 'encoder.9.cv1.norm.bias', 'encoder.9.cv1.norm.running_mean', 'encoder.9.cv1.norm.running_var', 'encoder.9.cv1.norm.num_batches_tracked', 'encoder.9.cv2.0.conv1.conv.weight', 'encoder.9.cv2.0.conv1.norm.weight', 'encoder.9.cv2.0.conv1.norm.bias', 'encoder.9.cv2.0.conv1.norm.running_mean', 'encoder.9.cv2.0.conv1.norm.running_var', 'encoder.9.cv2.0.conv1.norm.num_batches_tracked', 'encoder.9.cv2.0.conv2.conv.weight', 'encoder.9.cv2.0.conv2.norm.weight', 'encoder.9.cv2.0.conv2.norm.bias', 'encoder.9.cv2.0.conv2.norm.running_mean', 'encoder.9.cv2.0.conv2.norm.running_var', 'encoder.9.cv2.0.conv2.norm.num_batches_tracked', 'encoder.9.cv2.0.bottlenecks.0.conv1.conv.weight', 'encoder.9.cv2.0.bottlenecks.0.conv1.norm.weight', 'encoder.9.cv2.0.bottlenecks.0.conv1.norm.bias', 'encoder.9.cv2.0.bottlenecks.0.conv1.norm.running_mean', 'encoder.9.cv2.0.bottlenecks.0.conv1.norm.running_var', 'encoder.9.cv2.0.bottlenecks.0.conv1.norm.num_batches_tracked', 'encoder.9.cv2.0.bottlenecks.0.conv2.conv.weight', 'encoder.9.cv2.0.bottlenecks.0.conv2.norm.weight', 'encoder.9.cv2.0.bottlenecks.0.conv2.norm.bias', 'encoder.9.cv2.0.bottlenecks.0.conv2.norm.running_mean', 'encoder.9.cv2.0.bottlenecks.0.conv2.norm.running_var', 'encoder.9.cv2.0.bottlenecks.0.conv2.norm.num_batches_tracked', 'encoder.9.cv2.0.bottlenecks.1.conv1.conv.weight', 'encoder.9.cv2.0.bottlenecks.1.conv1.norm.weight', 'encoder.9.cv2.0.bottlenecks.1.conv1.norm.bias', 'encoder.9.cv2.0.bottlenecks.1.conv1.norm.running_mean', 'encoder.9.cv2.0.bottlenecks.1.conv1.norm.running_var', 'encoder.9.cv2.0.bottlenecks.1.conv1.norm.num_batches_tracked', 'encoder.9.cv2.0.bottlenecks.1.conv2.conv.weight', 'encoder.9.cv2.0.bottlenecks.1.conv2.norm.weight', 'encoder.9.cv2.0.bottlenecks.1.conv2.norm.bias', 'encoder.9.cv2.0.bottlenecks.1.conv2.norm.running_mean', 'encoder.9.cv2.0.bottlenecks.1.conv2.norm.running_var', 'encoder.9.cv2.0.bottlenecks.1.conv2.norm.num_batches_tracked', 'encoder.9.cv2.1.conv.weight', 'encoder.9.cv2.1.norm.weight', 'encoder.9.cv2.1.norm.bias', 'encoder.9.cv2.1.norm.running_mean', 'encoder.9.cv2.1.norm.running_var', 'encoder.9.cv2.1.norm.num_batches_tracked', 'encoder.9.cv3.0.conv1.conv.weight', 'encoder.9.cv3.0.conv1.norm.weight', 'encoder.9.cv3.0.conv1.norm.bias', 'encoder.9.cv3.0.conv1.norm.running_mean', 'encoder.9.cv3.0.conv1.norm.running_var', 'encoder.9.cv3.0.conv1.norm.num_batches_tracked', 'encoder.9.cv3.0.conv2.conv.weight', 'encoder.9.cv3.0.conv2.norm.weight', 'encoder.9.cv3.0.conv2.norm.bias', 'encoder.9.cv3.0.conv2.norm.running_mean', 'encoder.9.cv3.0.conv2.norm.running_var', 'encoder.9.cv3.0.conv2.norm.num_batches_tracked', 'encoder.9.cv3.0.bottlenecks.0.conv1.conv.weight', 'encoder.9.cv3.0.bottlenecks.0.conv1.norm.weight', 'encoder.9.cv3.0.bottlenecks.0.conv1.norm.bias', 'encoder.9.cv3.0.bottlenecks.0.conv1.norm.running_mean', 'encoder.9.cv3.0.bottlenecks.0.conv1.norm.running_var', 'encoder.9.cv3.0.bottlenecks.0.conv1.norm.num_batches_tracked', 'encoder.9.cv3.0.bottlenecks.0.conv2.conv.weight', 'encoder.9.cv3.0.bottlenecks.0.conv2.norm.weight', 'encoder.9.cv3.0.bottlenecks.0.conv2.norm.bias', 'encoder.9.cv3.0.bottlenecks.0.conv2.norm.running_mean', 'encoder.9.cv3.0.bottlenecks.0.conv2.norm.running_var', 'encoder.9.cv3.0.bottlenecks.0.conv2.norm.num_batches_tracked', 'encoder.9.cv3.0.bottlenecks.1.conv1.conv.weight', 'encoder.9.cv3.0.bottlenecks.1.conv1.norm.weight', 'encoder.9.cv3.0.bottlenecks.1.conv1.norm.bias', 'encoder.9.cv3.0.bottlenecks.1.conv1.norm.running_mean', 'encoder.9.cv3.0.bottlenecks.1.conv1.norm.running_var', 'encoder.9.cv3.0.bottlenecks.1.conv1.norm.num_batches_tracked', 'encoder.9.cv3.0.bottlenecks.1.conv2.conv.weight', 'encoder.9.cv3.0.bottlenecks.1.conv2.norm.weight', 'encoder.9.cv3.0.bottlenecks.1.conv2.norm.bias', 'encoder.9.cv3.0.bottlenecks.1.conv2.norm.running_mean', 'encoder.9.cv3.0.bottlenecks.1.conv2.norm.running_var', 'encoder.9.cv3.0.bottlenecks.1.conv2.norm.num_batches_tracked', 'encoder.9.cv3.1.conv.weight', 'encoder.9.cv3.1.norm.weight', 'encoder.9.cv3.1.norm.bias', 'encoder.9.cv3.1.norm.running_mean', 'encoder.9.cv3.1.norm.running_var', 'encoder.9.cv3.1.norm.num_batches_tracked', 'encoder.9.cv4.conv.weight', 'encoder.9.cv4.norm.weight', 'encoder.9.cv4.norm.bias', 'encoder.9.cv4.norm.running_mean', 'encoder.9.cv4.norm.running_var', 'encoder.9.cv4.norm.num_batches_tracked', 'decoder.denoising_class_embed.weight'], 'unmatched': ['decoder.enc_score_head.weight', 'decoder.enc_score_head.bias', 'decoder.dec_score_head.0.weight', 'decoder.dec_score_head.0.bias', 'decoder.dec_score_head.1.weight', 'decoder.dec_score_head.1.bias', 'decoder.dec_score_head.2.weight', 'decoder.dec_score_head.2.bias']}
2026-01-20 15:38:48 [_solver.py:_setup:103] INFO: output_dir:outputs\deim_hgnetv2_n_custom
2026-01-20 15:38:48 [yaml_config.py:lr_scheduler:179] INFO: Initial lr: [0.0004, 0.0004, 0.0008, 0.0008]
2026-01-20 15:38:48 [yaml_config.py:build_dataloader:291] INFO: building train_dataloader with batch_size=8...
2026-01-20 15:38:48 [container.py:__init__:36] INFO:      ### Transform @Mosaic ###    
2026-01-20 15:38:48 [container.py:__init__:36] INFO:      ### Transform @RandomPhotometricDistort ###    
2026-01-20 15:38:48 [container.py:__init__:36] INFO:      ### Transform @RandomZoomOut ###    
2026-01-20 15:38:48 [container.py:__init__:36] INFO:      ### Transform @RandomIoUCrop ###    
2026-01-20 15:38:48 [container.py:__init__:36] INFO:      ### Transform @SanitizeBoundingBoxes ###    
2026-01-20 15:38:48 [container.py:__init__:36] INFO:      ### Transform @RandomHorizontalFlip ###    
2026-01-20 15:38:48 [container.py:__init__:36] INFO:      ### Transform @Resize ###    
2026-01-20 15:38:48 [container.py:__init__:36] INFO:      ### Transform @SanitizeBoundingBoxes ###    
2026-01-20 15:38:48 [container.py:__init__:36] INFO:      ### Transform @ConvertPILImage ###    
2026-01-20 15:38:48 [container.py:__init__:36] INFO:      ### Transform @ConvertBoxes ###    
2026-01-20 15:38:48 [container.py:__init__:53] INFO:      ### Mosaic with Prob.@0.5 and ZoomOut/IoUCrop existed ### 
2026-01-20 15:38:48 [container.py:__init__:54] INFO:      ### ImgTransforms Epochs: [4, 194, 380] ### 
2026-01-20 15:38:48 [container.py:__init__:55] INFO:      ### Policy_ops@['Mosaic', 'RandomPhotometricDistort', 'RandomZoomOut', 'RandomIoUCrop'] ###
Caching images (1.0GB Ram: 100%|██████████| 1147/1147 [00:05<00:00, 199.02it/s]
2026-01-20 15:38:54 [dataloader.py:__init__:140] INFO:      ### Using MixUp with Prob@0.4 in [4, 194] epochs ### 
2026-01-20 15:38:54 [dataloader.py:__init__:149] INFO:      ### Multi-scale Training until 380 epochs ### 
2026-01-20 15:38:54 [dataloader.py:__init__:150] INFO:      ### Multi-scales@ None ###        
2026-01-20 15:38:54 [yaml_config.py:build_dataloader:291] INFO: building val_dataloader with batch_size=8...
2026-01-20 15:38:54 [container.py:__init__:36] INFO:      ### Transform @Resize ###    
2026-01-20 15:38:54 [container.py:__init__:36] INFO:      ### Transform @ConvertPILImage ###    
Caching images (0.2GB Ram: 100%|██████████| 181/181 [00:00<00:00, 238.73it/s]

------------------------------------- Calculate Flops Results -------------------------------------
Notations:
number of parameters (Params), number of multiply-accumulate operations(MACs),
number of floating-point operations (FLOPs), floating-point operations per second (FLOPS),
fwd FLOPs (model forward propagation FLOPs), bwd FLOPs (model backward propagation FLOPs),
default model backpropagation takes 2.00 times as much computation as forward propagation.

Total Training Params:                                                  3.73 M  
fwd MACs:                                                               3.5292 GMACs
fwd FLOPs:                                                              7.1217 GFLOPS
fwd+bwd MACs:                                                           10.5877 GMACs
fwd+bwd FLOPs:                                                          21.3652 GFLOPS
---------------------------------------------------------------------------------------------------
{'Model FLOPs:7.1217 GFLOPS   MACs:3.5292 GMACs   Params:3725365'}
2026-01-20 15:38:55 [det_solver.py:fit:44] INFO: Start training
2026-01-20 15:38:55 [det_solver.py:fit:51] INFO:      ## Using Self-defined Scheduler-flatcosine ## 
2026-01-20 15:38:55 [lr_scheduler.py:__init__:95] INFO: [0.0004, 0.0004, 0.0008, 0.0008], [0.00032, 0.00032, 0.00064, 0.00064], 57200, 2000, 27742, 2860
Epoch: 0/400:   0%|          | 0/143 [00:00<?, ?batch/s]2026-01-20 15:38:56 [det_solver.py:fit:58] INFO: number of trainable parameters: 3735679
Epoch: 0/400: 100%|██████████| 143/143 [03:33<00:00,  1.49s/batch, d_t=0.0002, it_t=0.2673, memory=2,949 MB, meters=lr: 0.000002  loss: 47.5595 (48.8060)  loss_mal: 1.2559 (1.2080)  loss_bbox: 1.4610 (1.5146)  loss_giou: 1.6176 (1.6474)  loss_fgl: 1.1795 (1.2694)  loss_mal_aux_0: 1.3053 (1.2236)  loss_bbox_aux_0: 1.5923 (1.6579)  loss_giou_aux_0: 1.6336 (1.6496)  loss_fgl_aux_0: 1.2339 (1.2855)  loss_ddf_aux_0: 0.1259 (0.1314)  loss_mal_aux_1: 1.2504 (1.2140)  loss_bbox_aux_1: 1.4722 (1.5319)  loss_giou_aux_1: 1.6118 (1.6353)  loss_fgl_aux_1: 1.2090 (1.2906)  loss_ddf_aux_1: 0.0172 (0.0179)  loss_mal_pre: 1.2678 (1.2797)  loss_bbox_pre: 1.5632 (1.5801)  loss_giou_pre: 1.5717 (1.5867)  loss_mal_enc_0: 1.0563 (1.1027)  loss_bbox_enc_0: 1.6364 (1.5829)  loss_giou_enc_0: 1.6912 (1.7032)  loss_mal_dn_0: 0.7681 (0.7328)  loss_bbox_dn_0: 2.2153 (2.4356)  loss_giou_dn_0: 1.7187 (1.7897)  loss_fgl_dn_0: 1.2379 (1.2332)  loss_ddf_dn_0: 0.1200 (0.1252)  loss_mal_dn_1: 0.8080 (0.7810)  loss_bbox_dn_1: 2.0131 (2.2271)  loss_giou_dn_1: 1.7093 (1.7713)  loss_fgl_dn_1: 1.1943 (1.1906)  loss_ddf_dn_1: 0.0141 (0.0155)  loss_mal_dn_2: 0.7814 (0.7508)  loss_bbox_dn_2: 1.9369 (2.1156)  loss_giou_dn_2: 1.7112 (1.7705)  loss_fgl_dn_2: 1.2094 (1.1938)  loss_mal_dn_pre: 0.8697 (0.8217)  loss_bbox_dn_pre: 2.0373 (2.0931)  loss_giou_dn_pre: 1.6024 (1.6462)]
2026-01-20 15:42:30 [logger.py:log_every:345] INFO: Epoch: 0/400 Total time: 0:03:33 (1.4949 s / it)
2026-01-20 15:42:30 [det_engine.py:train_one_epoch:187] INFO: Averaged stats:lr: 0.000002  loss: 47.5595 (48.8060)  loss_mal: 1.2559 (1.2080)  loss_bbox: 1.4610 (1.5146)  loss_giou: 1.6176 (1.6474)  loss_fgl: 1.1795 (1.2694)  loss_mal_aux_0: 1.3053 (1.2236)  loss_bbox_aux_0: 1.5923 (1.6579)  loss_giou_aux_0: 1.6336 (1.6496)  loss_fgl_aux_0: 1.2339 (1.2855)  loss_ddf_aux_0: 0.1259 (0.1314)  loss_mal_aux_1: 1.2504 (1.2140)  loss_bbox_aux_1: 1.4722 (1.5319)  loss_giou_aux_1: 1.6118 (1.6353)  loss_fgl_aux_1: 1.2090 (1.2906)  loss_ddf_aux_1: 0.0172 (0.0179)  loss_mal_pre: 1.2678 (1.2797)  loss_bbox_pre: 1.5632 (1.5801)  loss_giou_pre: 1.5717 (1.5867)  loss_mal_enc_0: 1.0563 (1.1027)  loss_bbox_enc_0: 1.6364 (1.5829)  loss_giou_enc_0: 1.6912 (1.7032)  loss_mal_dn_0: 0.7681 (0.7328)  loss_bbox_dn_0: 2.2153 (2.4356)  loss_giou_dn_0: 1.7187 (1.7897)  loss_fgl_dn_0: 1.2379 (1.2332)  loss_ddf_dn_0: 0.1200 (0.1252)  loss_mal_dn_1: 0.8080 (0.7810)  loss_bbox_dn_1: 2.0131 (2.2271)  loss_giou_dn_1: 1.7093 (1.7713)  loss_fgl_dn_1: 1.1943 (1.1906)  loss_ddf_dn_1: 0.0141 (0.0155)  loss_mal_dn_2: 0.7814 (0.7508)  loss_bbox_dn_2: 1.9369 (2.1156)  loss_giou_dn_2: 1.7112 (1.7705)  loss_fgl_dn_2: 1.2094 (1.1938)  loss_mal_dn_pre: 0.8697 (0.8217)  loss_bbox_dn_pre: 2.0373 (2.0931)  loss_giou_dn_pre: 1.6024 (1.6462)
Test:: 100%|██████████| 23/23 [00:32<00:00,  1.42s/batch, d_t=0.0006, it_t=0.0749, memory=2,949 MB, meters=]
2026-01-20 15:43:03 [logger.py:log_every:345] INFO: Test: Total time: 0:00:32 (1.4248 s / it)
2026-01-20 15:43:03 [yolo_metrice.py:get_yolo_det_metrice:380] INFO: ------------------------ YOLO Metrics[bbox] Start ------------------------
2026-01-20 15:43:03 [yolo_metrice.py:get_yolo_det_metrice:381] INFO: ------------------------ YOLO指标和COCO指标有差异属于正常情况 ------------------------
Cal YOLO(bbox) mAP...: 100%|██████████| 181/181 [00:00<00:00, 3060.04it/s]
+--------------------------------------------------------------------------+
|                            YOLO Metrics(bbox)                            |
+---------------+-----------+--------+----------+-------+-------+----------+
|    Classes    | Precision | Recall | F1-Score | mAP50 | mAP75 | mAP50-95 |
+---------------+-----------+--------+----------+-------+-------+----------+
|      all      |   0.000   | 0.014  |  0.000   | 0.000 | 0.000 |  0.000   |
|   BackCorner  |   0.001   | 0.025  |  0.001   | 0.000 | 0.000 |  0.000   |
|  FrontCorner  |   0.000   | 0.047  |  0.000   | 0.000 | 0.000 |  0.000   |
| FrontDownBeam |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|    BackBeam   |   0.000   | 0.029  |  0.000   | 0.000 | 0.000 |  0.000   |
|  FrontUpBeam  |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|    BackFoot   |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|   FrontFoot   |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
+---------------+-----------+--------+----------+-------+-------+----------+
2026-01-20 15:43:04 [det_engine.py:evaluate:303] INFO: ------------------------ COCO Metrice Start ------------------------
2026-01-20 15:43:04 [coco_eval.py:summarize:102] INFO: IoU metric:bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.001
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.002
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.002
2026-01-20 15:43:04 [det_solver.py:save_best_model:595] INFO: Current metrics: {'coco_eval_bbox': 9.803322608940578e-07}
2026-01-20 15:43:04 [det_solver.py:save_best_model:596] INFO: Current avg: 0.0000, Best avg: 0.0000 (epoch 0)
2026-01-20 15:43:04 [det_solver.py:save_best_model:600] INFO: 🎉 New Best Model!
2026-01-20 15:43:04 [det_solver.py:save_best_model:601] INFO:   Epoch: -1 -> 0
2026-01-20 15:43:04 [det_solver.py:save_best_model:602] INFO:   Avg AP: 0.0000 -> 0.0000
2026-01-20 15:43:04 [det_solver.py:save_best_model:608] INFO:   coco_eval_bbox: 0.0000 -> 0.0000
Epoch: 1/400:   0%|          | 0/143 [00:00<?, ?batch/s]2026-01-20 15:43:04 [det_solver.py:save_best_model:618] INFO: 💾 Saved best_stg1.pth
Epoch: 1/400: 100%|██████████| 143/143 [03:09<00:00,  1.32s/batch, d_t=0.0003, it_t=0.2578, memory=2,949 MB, meters=lr: 0.000008  loss: 43.0850 (45.3994)  loss_mal: 1.2764 (1.2623)  loss_bbox: 1.2210 (1.3107)  loss_giou: 1.4679 (1.5198)  loss_fgl: 1.0544 (1.1964)  loss_mal_aux_0: 1.2670 (1.2979)  loss_bbox_aux_0: 1.2367 (1.3958)  loss_giou_aux_0: 1.4007 (1.5031)  loss_fgl_aux_0: 1.0908 (1.2224)  loss_ddf_aux_0: 0.1034 (0.1213)  loss_mal_aux_1: 1.3246 (1.2702)  loss_bbox_aux_1: 1.2367 (1.3131)  loss_giou_aux_1: 1.4593 (1.5075)  loss_fgl_aux_1: 1.0673 (1.2123)  loss_ddf_aux_1: 0.0130 (0.0159)  loss_mal_pre: 1.2359 (1.3362)  loss_bbox_pre: 1.2954 (1.4056)  loss_giou_pre: 1.4287 (1.4770)  loss_mal_enc_0: 1.1075 (1.1304)  loss_bbox_enc_0: 1.4379 (1.4878)  loss_giou_enc_0: 1.5550 (1.6184)  loss_mal_dn_0: 0.9702 (0.8695)  loss_bbox_dn_0: 1.5673 (1.9103)  loss_giou_dn_0: 1.4949 (1.6199)  loss_fgl_dn_0: 1.1535 (1.2081)  loss_ddf_dn_0: 0.1019 (0.1152)  loss_mal_dn_1: 1.0271 (0.9446)  loss_bbox_dn_1: 1.4580 (1.7389)  loss_giou_dn_1: 1.4974 (1.6015)  loss_fgl_dn_1: 1.1123 (1.1616)  loss_ddf_dn_1: 0.0125 (0.0140)  loss_mal_dn_2: 0.9768 (0.8950)  loss_bbox_dn_2: 1.4171 (1.6781)  loss_giou_dn_2: 1.4984 (1.6020)  loss_fgl_dn_2: 1.1163 (1.1612)  loss_mal_dn_pre: 0.9885 (0.9243)  loss_bbox_dn_pre: 1.5712 (1.8019)  loss_giou_dn_pre: 1.4856 (1.5491)]
2026-01-20 15:46:13 [logger.py:log_every:345] INFO: Epoch: 1/400 Total time: 0:03:09 (1.3244 s / it)
2026-01-20 15:46:13 [det_engine.py:train_one_epoch:187] INFO: Averaged stats:lr: 0.000008  loss: 43.0850 (45.3994)  loss_mal: 1.2764 (1.2623)  loss_bbox: 1.2210 (1.3107)  loss_giou: 1.4679 (1.5198)  loss_fgl: 1.0544 (1.1964)  loss_mal_aux_0: 1.2670 (1.2979)  loss_bbox_aux_0: 1.2367 (1.3958)  loss_giou_aux_0: 1.4007 (1.5031)  loss_fgl_aux_0: 1.0908 (1.2224)  loss_ddf_aux_0: 0.1034 (0.1213)  loss_mal_aux_1: 1.3246 (1.2702)  loss_bbox_aux_1: 1.2367 (1.3131)  loss_giou_aux_1: 1.4593 (1.5075)  loss_fgl_aux_1: 1.0673 (1.2123)  loss_ddf_aux_1: 0.0130 (0.0159)  loss_mal_pre: 1.2359 (1.3362)  loss_bbox_pre: 1.2954 (1.4056)  loss_giou_pre: 1.4287 (1.4770)  loss_mal_enc_0: 1.1075 (1.1304)  loss_bbox_enc_0: 1.4379 (1.4878)  loss_giou_enc_0: 1.5550 (1.6184)  loss_mal_dn_0: 0.9702 (0.8695)  loss_bbox_dn_0: 1.5673 (1.9103)  loss_giou_dn_0: 1.4949 (1.6199)  loss_fgl_dn_0: 1.1535 (1.2081)  loss_ddf_dn_0: 0.1019 (0.1152)  loss_mal_dn_1: 1.0271 (0.9446)  loss_bbox_dn_1: 1.4580 (1.7389)  loss_giou_dn_1: 1.4974 (1.6015)  loss_fgl_dn_1: 1.1123 (1.1616)  loss_ddf_dn_1: 0.0125 (0.0140)  loss_mal_dn_2: 0.9768 (0.8950)  loss_bbox_dn_2: 1.4171 (1.6781)  loss_giou_dn_2: 1.4984 (1.6020)  loss_fgl_dn_2: 1.1163 (1.1612)  loss_mal_dn_pre: 0.9885 (0.9243)  loss_bbox_dn_pre: 1.5712 (1.8019)  loss_giou_dn_pre: 1.4856 (1.5491)
Test:: 100%|██████████| 23/23 [00:31<00:00,  1.35s/batch, d_t=0.0003, it_t=0.0712, memory=2,949 MB, meters=]
2026-01-20 15:46:46 [logger.py:log_every:345] INFO: Test: Total time: 0:00:31 (1.3519 s / it)
2026-01-20 15:46:46 [yolo_metrice.py:get_yolo_det_metrice:380] INFO: ------------------------ YOLO Metrics[bbox] Start ------------------------
2026-01-20 15:46:46 [yolo_metrice.py:get_yolo_det_metrice:381] INFO: ------------------------ YOLO指标和COCO指标有差异属于正常情况 ------------------------
Cal YOLO(bbox) mAP...: 100%|██████████| 181/181 [00:00<00:00, 3404.24it/s]
+--------------------------------------------------------------------------+
|                            YOLO Metrics(bbox)                            |
+---------------+-----------+--------+----------+-------+-------+----------+
|    Classes    | Precision | Recall | F1-Score | mAP50 | mAP75 | mAP50-95 |
+---------------+-----------+--------+----------+-------+-------+----------+
|      all      |   0.000   | 0.018  |  0.000   | 0.000 | 0.000 |  0.000   |
|   BackCorner  |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|  FrontCorner  |   0.000   | 0.031  |  0.000   | 0.000 | 0.000 |  0.000   |
| FrontDownBeam |   0.000   | 0.019  |  0.000   | 0.000 | 0.000 |  0.000   |
|    BackBeam   |   0.000   | 0.029  |  0.000   | 0.000 | 0.000 |  0.000   |
|  FrontUpBeam  |   0.000   | 0.048  |  0.001   | 0.000 | 0.000 |  0.000   |
|    BackFoot   |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|   FrontFoot   |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
+---------------+-----------+--------+----------+-------+-------+----------+
2026-01-20 15:46:46 [det_engine.py:evaluate:303] INFO: ------------------------ COCO Metrice Start ------------------------
2026-01-20 15:46:46 [coco_eval.py:summarize:102] INFO: IoU metric:bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.002
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.003
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.002
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.003
2026-01-20 15:46:46 [det_solver.py:save_best_model:595] INFO: Current metrics: {'coco_eval_bbox': 7.731861551005794e-06}
2026-01-20 15:46:46 [det_solver.py:save_best_model:596] INFO: Current avg: 0.0000, Best avg: 0.0000 (epoch 1)
2026-01-20 15:46:46 [det_solver.py:save_best_model:600] INFO: 🎉 New Best Model!
2026-01-20 15:46:46 [det_solver.py:save_best_model:601] INFO:   Epoch: 0 -> 1
2026-01-20 15:46:46 [det_solver.py:save_best_model:602] INFO:   Avg AP: 0.0000 -> 0.0000
2026-01-20 15:46:46 [det_solver.py:save_best_model:608] INFO:   coco_eval_bbox: 0.0000 -> 0.0000
2026-01-20 15:46:46 [det_solver.py:save_best_model:618] INFO: 💾 Saved best_stg1.pth
Epoch: 2/400: 100%|██████████| 143/143 [03:14<00:00,  1.36s/batch, d_t=0.0005, it_t=0.2845, memory=2,949 MB, meters=lr: 0.000018  loss: 40.6832 (41.5249)  loss_mal: 1.6316 (1.4346)  loss_bbox: 0.9931 (1.1002)  loss_giou: 1.2149 (1.3639)  loss_fgl: 1.0213 (1.0293)  loss_mal_aux_0: 1.5678 (1.4204)  loss_bbox_aux_0: 1.0799 (1.1182)  loss_giou_aux_0: 1.2448 (1.3454)  loss_fgl_aux_0: 1.0346 (1.0571)  loss_ddf_aux_0: 0.0663 (0.0869)  loss_mal_aux_1: 1.6827 (1.5053)  loss_bbox_aux_1: 0.9906 (1.0909)  loss_giou_aux_1: 1.2403 (1.3542)  loss_fgl_aux_1: 1.0166 (1.0388)  loss_ddf_aux_1: 0.0082 (0.0110)  loss_mal_pre: 1.5606 (1.4118)  loss_bbox_pre: 1.0646 (1.1680)  loss_giou_pre: 1.2622 (1.3533)  loss_mal_enc_0: 1.3745 (1.2760)  loss_bbox_enc_0: 1.1134 (1.2259)  loss_giou_enc_0: 1.3126 (1.4381)  loss_mal_dn_0: 1.0853 (1.0508)  loss_bbox_dn_0: 1.2756 (1.4056)  loss_giou_dn_0: 1.4084 (1.4414)  loss_fgl_dn_0: 0.9889 (1.0685)  loss_ddf_dn_0: 0.0585 (0.0829)  loss_mal_dn_1: 1.2286 (1.1668)  loss_bbox_dn_1: 1.2145 (1.3010)  loss_giou_dn_1: 1.3922 (1.4304)  loss_fgl_dn_1: 0.9514 (1.0239)  loss_ddf_dn_1: 0.0062 (0.0095)  loss_mal_dn_2: 1.1254 (1.0776)  loss_bbox_dn_2: 1.1913 (1.2837)  loss_giou_dn_2: 1.3914 (1.4286)  loss_fgl_dn_2: 0.9515 (1.0232)  loss_mal_dn_pre: 1.0938 (1.0754)  loss_bbox_dn_pre: 1.2786 (1.4054)  loss_giou_dn_pre: 1.4021 (1.4208)]
2026-01-20 15:50:00 [logger.py:log_every:345] INFO: Epoch: 2/400 Total time: 0:03:14 (1.3586 s / it)
2026-01-20 15:50:00 [det_engine.py:train_one_epoch:187] INFO: Averaged stats:lr: 0.000018  loss: 40.6832 (41.5249)  loss_mal: 1.6316 (1.4346)  loss_bbox: 0.9931 (1.1002)  loss_giou: 1.2149 (1.3639)  loss_fgl: 1.0213 (1.0293)  loss_mal_aux_0: 1.5678 (1.4204)  loss_bbox_aux_0: 1.0799 (1.1182)  loss_giou_aux_0: 1.2448 (1.3454)  loss_fgl_aux_0: 1.0346 (1.0571)  loss_ddf_aux_0: 0.0663 (0.0869)  loss_mal_aux_1: 1.6827 (1.5053)  loss_bbox_aux_1: 0.9906 (1.0909)  loss_giou_aux_1: 1.2403 (1.3542)  loss_fgl_aux_1: 1.0166 (1.0388)  loss_ddf_aux_1: 0.0082 (0.0110)  loss_mal_pre: 1.5606 (1.4118)  loss_bbox_pre: 1.0646 (1.1680)  loss_giou_pre: 1.2622 (1.3533)  loss_mal_enc_0: 1.3745 (1.2760)  loss_bbox_enc_0: 1.1134 (1.2259)  loss_giou_enc_0: 1.3126 (1.4381)  loss_mal_dn_0: 1.0853 (1.0508)  loss_bbox_dn_0: 1.2756 (1.4056)  loss_giou_dn_0: 1.4084 (1.4414)  loss_fgl_dn_0: 0.9889 (1.0685)  loss_ddf_dn_0: 0.0585 (0.0829)  loss_mal_dn_1: 1.2286 (1.1668)  loss_bbox_dn_1: 1.2145 (1.3010)  loss_giou_dn_1: 1.3922 (1.4304)  loss_fgl_dn_1: 0.9514 (1.0239)  loss_ddf_dn_1: 0.0062 (0.0095)  loss_mal_dn_2: 1.1254 (1.0776)  loss_bbox_dn_2: 1.1913 (1.2837)  loss_giou_dn_2: 1.3914 (1.4286)  loss_fgl_dn_2: 0.9515 (1.0232)  loss_mal_dn_pre: 1.0938 (1.0754)  loss_bbox_dn_pre: 1.2786 (1.4054)  loss_giou_dn_pre: 1.4021 (1.4208)
Test:: 100%|██████████| 23/23 [00:31<00:00,  1.37s/batch, d_t=0.0004, it_t=0.0818, memory=2,949 MB, meters=]
2026-01-20 15:50:33 [logger.py:log_every:345] INFO: Test: Total time: 0:00:31 (1.3729 s / it)
2026-01-20 15:50:33 [yolo_metrice.py:get_yolo_det_metrice:380] INFO: ------------------------ YOLO Metrics[bbox] Start ------------------------
2026-01-20 15:50:33 [yolo_metrice.py:get_yolo_det_metrice:381] INFO: ------------------------ YOLO指标和COCO指标有差异属于正常情况 ------------------------
Cal YOLO(bbox) mAP...: 100%|██████████| 181/181 [00:00<00:00, 3227.24it/s]
+--------------------------------------------------------------------------+
|                            YOLO Metrics(bbox)                            |
+---------------+-----------+--------+----------+-------+-------+----------+
|    Classes    | Precision | Recall | F1-Score | mAP50 | mAP75 | mAP50-95 |
+---------------+-----------+--------+----------+-------+-------+----------+
|      all      |   0.000   | 0.026  |  0.000   | 0.000 | 0.000 |  0.000   |
|   BackCorner  |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|  FrontCorner  |   0.000   | 0.078  |  0.001   | 0.000 | 0.000 |  0.000   |
| FrontDownBeam |   0.000   | 0.074  |  0.001   | 0.000 | 0.000 |  0.000   |
|    BackBeam   |   0.000   | 0.029  |  0.000   | 0.000 | 0.000 |  0.000   |
|  FrontUpBeam  |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|    BackFoot   |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|   FrontFoot   |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
+---------------+-----------+--------+----------+-------+-------+----------+
2026-01-20 15:50:33 [det_engine.py:evaluate:303] INFO: ------------------------ COCO Metrice Start ------------------------
2026-01-20 15:50:33 [coco_eval.py:summarize:102] INFO: IoU metric:bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.001
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.005
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.006
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.004
2026-01-20 15:50:34 [det_solver.py:save_best_model:595] INFO: Current metrics: {'coco_eval_bbox': 2.6209332561356927e-06}
2026-01-20 15:50:34 [det_solver.py:save_best_model:596] INFO: Current avg: 0.0000, Best avg: 0.0000 (epoch 1)
Epoch: 3/400: 100%|██████████| 143/143 [03:12<00:00,  1.35s/batch, d_t=0.0004, it_t=0.3560, memory=2,949 MB, meters=lr: 0.000033  loss: 38.0662 (39.0575)  loss_mal: 1.9457 (1.7102)  loss_bbox: 0.7076 (0.8474)  loss_giou: 0.9699 (1.1251)  loss_fgl: 1.0857 (1.0477)  loss_mal_aux_0: 1.8027 (1.6659)  loss_bbox_aux_0: 0.7494 (0.8765)  loss_giou_aux_0: 1.0210 (1.1391)  loss_fgl_aux_0: 1.0706 (1.0380)  loss_ddf_aux_0: 0.0481 (0.0513)  loss_mal_aux_1: 1.9383 (1.7955)  loss_bbox_aux_1: 0.7052 (0.8472)  loss_giou_aux_1: 0.9911 (1.1338)  loss_fgl_aux_1: 1.0841 (1.0425)  loss_ddf_aux_1: 0.0085 (0.0075)  loss_mal_pre: 1.7873 (1.6631)  loss_bbox_pre: 0.7595 (0.8988)  loss_giou_pre: 1.0454 (1.1477)  loss_mal_enc_0: 1.7582 (1.5861)  loss_bbox_enc_0: 0.7840 (0.9415)  loss_giou_enc_0: 1.0300 (1.1825)  loss_mal_dn_0: 1.0264 (1.0758)  loss_bbox_dn_0: 1.1615 (1.1965)  loss_giou_dn_0: 1.3585 (1.3775)  loss_fgl_dn_0: 0.8783 (0.9259)  loss_ddf_dn_0: 0.0421 (0.0456)  loss_mal_dn_1: 1.1294 (1.2032)  loss_bbox_dn_1: 1.0906 (1.1317)  loss_giou_dn_1: 1.3249 (1.3556)  loss_fgl_dn_1: 0.8698 (0.9010)  loss_ddf_dn_1: 0.0046 (0.0048)  loss_mal_dn_2: 0.9723 (1.0509)  loss_bbox_dn_2: 1.0754 (1.1275)  loss_giou_dn_2: 1.3052 (1.3429)  loss_fgl_dn_2: 0.8766 (0.9062)  loss_mal_dn_pre: 1.0501 (1.0953)  loss_bbox_dn_pre: 1.1621 (1.1973)  loss_giou_dn_pre: 1.3627 (1.3723)]
2026-01-20 15:53:46 [logger.py:log_every:345] INFO: Epoch: 3/400 Total time: 0:03:12 (1.3477 s / it)
2026-01-20 15:53:46 [det_engine.py:train_one_epoch:187] INFO: Averaged stats:lr: 0.000033  loss: 38.0662 (39.0575)  loss_mal: 1.9457 (1.7102)  loss_bbox: 0.7076 (0.8474)  loss_giou: 0.9699 (1.1251)  loss_fgl: 1.0857 (1.0477)  loss_mal_aux_0: 1.8027 (1.6659)  loss_bbox_aux_0: 0.7494 (0.8765)  loss_giou_aux_0: 1.0210 (1.1391)  loss_fgl_aux_0: 1.0706 (1.0380)  loss_ddf_aux_0: 0.0481 (0.0513)  loss_mal_aux_1: 1.9383 (1.7955)  loss_bbox_aux_1: 0.7052 (0.8472)  loss_giou_aux_1: 0.9911 (1.1338)  loss_fgl_aux_1: 1.0841 (1.0425)  loss_ddf_aux_1: 0.0085 (0.0075)  loss_mal_pre: 1.7873 (1.6631)  loss_bbox_pre: 0.7595 (0.8988)  loss_giou_pre: 1.0454 (1.1477)  loss_mal_enc_0: 1.7582 (1.5861)  loss_bbox_enc_0: 0.7840 (0.9415)  loss_giou_enc_0: 1.0300 (1.1825)  loss_mal_dn_0: 1.0264 (1.0758)  loss_bbox_dn_0: 1.1615 (1.1965)  loss_giou_dn_0: 1.3585 (1.3775)  loss_fgl_dn_0: 0.8783 (0.9259)  loss_ddf_dn_0: 0.0421 (0.0456)  loss_mal_dn_1: 1.1294 (1.2032)  loss_bbox_dn_1: 1.0906 (1.1317)  loss_giou_dn_1: 1.3249 (1.3556)  loss_fgl_dn_1: 0.8698 (0.9010)  loss_ddf_dn_1: 0.0046 (0.0048)  loss_mal_dn_2: 0.9723 (1.0509)  loss_bbox_dn_2: 1.0754 (1.1275)  loss_giou_dn_2: 1.3052 (1.3429)  loss_fgl_dn_2: 0.8766 (0.9062)  loss_mal_dn_pre: 1.0501 (1.0953)  loss_bbox_dn_pre: 1.1621 (1.1973)  loss_giou_dn_pre: 1.3627 (1.3723)
Test:: 100%|██████████| 23/23 [00:35<00:00,  1.55s/batch, d_t=0.0005, it_t=0.0994, memory=2,949 MB, meters=]
2026-01-20 15:54:23 [logger.py:log_every:345] INFO: Test: Total time: 0:00:35 (1.5464 s / it)
2026-01-20 15:54:23 [yolo_metrice.py:get_yolo_det_metrice:380] INFO: ------------------------ YOLO Metrics[bbox] Start ------------------------
2026-01-20 15:54:23 [yolo_metrice.py:get_yolo_det_metrice:381] INFO: ------------------------ YOLO指标和COCO指标有差异属于正常情况 ------------------------
Cal YOLO(bbox) mAP...: 100%|██████████| 181/181 [00:00<00:00, 1142.05it/s]
+--------------------------------------------------------------------------+
|                            YOLO Metrics(bbox)                            |
+---------------+-----------+--------+----------+-------+-------+----------+
|    Classes    | Precision | Recall | F1-Score | mAP50 | mAP75 | mAP50-95 |
+---------------+-----------+--------+----------+-------+-------+----------+
|      all      |   0.001   | 0.217  |  0.001   | 0.001 | 0.000 |  0.000   |
|   BackCorner  |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|  FrontCorner  |   0.002   | 0.656  |  0.004   | 0.003 | 0.000 |  0.001   |
| FrontDownBeam |   0.001   | 0.333  |  0.002   | 0.001 | 0.000 |  0.000   |
|    BackBeam   |   0.002   | 0.529  |  0.004   | 0.002 | 0.000 |  0.000   |
|  FrontUpBeam  |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|    BackFoot   |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|   FrontFoot   |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
+---------------+-----------+--------+----------+-------+-------+----------+
2026-01-20 15:54:24 [det_engine.py:evaluate:303] INFO: ------------------------ COCO Metrice Start ------------------------
2026-01-20 15:54:24 [coco_eval.py:summarize:102] INFO: IoU metric:bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.001
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.015
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.060
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.023
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.064
2026-01-20 15:54:24 [det_solver.py:save_best_model:595] INFO: Current metrics: {'coco_eval_bbox': 0.0001221630575144833}
2026-01-20 15:54:24 [det_solver.py:save_best_model:596] INFO: Current avg: 0.0001, Best avg: 0.0001 (epoch 3)
2026-01-20 15:54:24 [det_solver.py:save_best_model:600] INFO: 🎉 New Best Model!
2026-01-20 15:54:24 [det_solver.py:save_best_model:601] INFO:   Epoch: 1 -> 3
2026-01-20 15:54:24 [det_solver.py:save_best_model:602] INFO:   Avg AP: 0.0000 -> 0.0001
2026-01-20 15:54:24 [det_solver.py:save_best_model:608] INFO:   coco_eval_bbox: 0.0000 -> 0.0001
Epoch: 4/400:   0%|          | 0/143 [00:00<?, ?batch/s]2026-01-20 15:54:25 [det_solver.py:save_best_model:618] INFO: 💾 Saved best_stg1.pth
Epoch: 4/400: 100%|██████████| 143/143 [03:16<00:00,  1.38s/batch, d_t=0.0002, it_t=0.2656, memory=2,949 MB, meters=lr: 0.000051  loss: 31.7176 (32.4988)  loss_mal: 1.3949 (1.2467)  loss_bbox: 0.5841 (0.6792)  loss_giou: 1.2454 (1.3226)  loss_fgl: 0.8466 (0.8231)  loss_mal_aux_0: 1.3659 (1.1509)  loss_bbox_aux_0: 0.5968 (0.6871)  loss_giou_aux_0: 1.2679 (1.3369)  loss_fgl_aux_0: 0.8373 (0.8153)  loss_ddf_aux_0: 0.0132 (0.0297)  loss_mal_aux_1: 1.3645 (1.1954)  loss_bbox_aux_1: 0.5827 (0.6781)  loss_giou_aux_1: 1.2470 (1.3302)  loss_fgl_aux_1: 0.8480 (0.8186)  loss_ddf_aux_1: 0.0036 (0.0065)  loss_mal_pre: 1.1765 (1.0972)  loss_bbox_pre: 0.5972 (0.6884)  loss_giou_pre: 1.2663 (1.3405)  loss_mal_enc_0: 1.1156 (1.0794)  loss_bbox_enc_0: 0.6081 (0.7033)  loss_giou_enc_0: 1.2859 (1.3475)  loss_mal_dn_0: 0.8023 (0.8818)  loss_bbox_dn_0: 0.5894 (0.6582)  loss_giou_dn_0: 1.3223 (1.3631)  loss_fgl_dn_0: 0.8342 (0.8473)  loss_ddf_dn_0: 0.0298 (0.0402)  loss_mal_dn_1: 0.8814 (0.9233)  loss_bbox_dn_1: 0.5482 (0.6320)  loss_giou_dn_1: 1.2519 (1.3227)  loss_fgl_dn_1: 0.8562 (0.8503)  loss_ddf_dn_1: 0.0052 (0.0057)  loss_mal_dn_2: 0.8824 (0.8642)  loss_bbox_dn_2: 0.5354 (0.6276)  loss_giou_dn_2: 1.2199 (1.3008)  loss_fgl_dn_2: 0.8644 (0.8570)  loss_mal_dn_pre: 0.8630 (0.9390)  loss_bbox_dn_pre: 0.5873 (0.6522)  loss_giou_dn_pre: 1.3255 (1.3567)]
2026-01-20 15:57:41 [logger.py:log_every:345] INFO: Epoch: 4/400 Total time: 0:03:16 (1.3759 s / it)
2026-01-20 15:57:41 [det_engine.py:train_one_epoch:187] INFO: Averaged stats:lr: 0.000051  loss: 31.7176 (32.4988)  loss_mal: 1.3949 (1.2467)  loss_bbox: 0.5841 (0.6792)  loss_giou: 1.2454 (1.3226)  loss_fgl: 0.8466 (0.8231)  loss_mal_aux_0: 1.3659 (1.1509)  loss_bbox_aux_0: 0.5968 (0.6871)  loss_giou_aux_0: 1.2679 (1.3369)  loss_fgl_aux_0: 0.8373 (0.8153)  loss_ddf_aux_0: 0.0132 (0.0297)  loss_mal_aux_1: 1.3645 (1.1954)  loss_bbox_aux_1: 0.5827 (0.6781)  loss_giou_aux_1: 1.2470 (1.3302)  loss_fgl_aux_1: 0.8480 (0.8186)  loss_ddf_aux_1: 0.0036 (0.0065)  loss_mal_pre: 1.1765 (1.0972)  loss_bbox_pre: 0.5972 (0.6884)  loss_giou_pre: 1.2663 (1.3405)  loss_mal_enc_0: 1.1156 (1.0794)  loss_bbox_enc_0: 0.6081 (0.7033)  loss_giou_enc_0: 1.2859 (1.3475)  loss_mal_dn_0: 0.8023 (0.8818)  loss_bbox_dn_0: 0.5894 (0.6582)  loss_giou_dn_0: 1.3223 (1.3631)  loss_fgl_dn_0: 0.8342 (0.8473)  loss_ddf_dn_0: 0.0298 (0.0402)  loss_mal_dn_1: 0.8814 (0.9233)  loss_bbox_dn_1: 0.5482 (0.6320)  loss_giou_dn_1: 1.2519 (1.3227)  loss_fgl_dn_1: 0.8562 (0.8503)  loss_ddf_dn_1: 0.0052 (0.0057)  loss_mal_dn_2: 0.8824 (0.8642)  loss_bbox_dn_2: 0.5354 (0.6276)  loss_giou_dn_2: 1.2199 (1.3008)  loss_fgl_dn_2: 0.8644 (0.8570)  loss_mal_dn_pre: 0.8630 (0.9390)  loss_bbox_dn_pre: 0.5873 (0.6522)  loss_giou_dn_pre: 1.3255 (1.3567)
Test:: 100%|██████████| 23/23 [00:29<00:00,  1.29s/batch, d_t=0.0004, it_t=0.0726, memory=2,949 MB, meters=]
2026-01-20 15:58:12 [logger.py:log_every:345] INFO: Test: Total time: 0:00:29 (1.2856 s / it)
2026-01-20 15:58:12 [yolo_metrice.py:get_yolo_det_metrice:380] INFO: ------------------------ YOLO Metrics[bbox] Start ------------------------
2026-01-20 15:58:12 [yolo_metrice.py:get_yolo_det_metrice:381] INFO: ------------------------ YOLO指标和COCO指标有差异属于正常情况 ------------------------
Cal YOLO(bbox) mAP...: 100%|██████████| 181/181 [00:00<00:00, 3217.54it/s]
+--------------------------------------------------------------------------+
|                            YOLO Metrics(bbox)                            |
+---------------+-----------+--------+----------+-------+-------+----------+
|    Classes    | Precision | Recall | F1-Score | mAP50 | mAP75 | mAP50-95 |
+---------------+-----------+--------+----------+-------+-------+----------+
|      all      |   0.000   | 0.077  |  0.001   | 0.001 | 0.000 |  0.000   |
|   BackCorner  |   0.000   | 0.050  |  0.000   | 0.000 | 0.000 |  0.000   |
|  FrontCorner  |   0.000   | 0.141  |  0.001   | 0.002 | 0.000 |  0.001   |
| FrontDownBeam |   0.002   | 0.204  |  0.004   | 0.001 | 0.000 |  0.000   |
|    BackBeam   |   0.000   | 0.147  |  0.001   | 0.000 | 0.000 |  0.000   |
|  FrontUpBeam  |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|    BackFoot   |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|   FrontFoot   |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
+---------------+-----------+--------+----------+-------+-------+----------+
2026-01-20 15:58:12 [det_engine.py:evaluate:303] INFO: ------------------------ COCO Metrice Start ------------------------
2026-01-20 15:58:12 [coco_eval.py:summarize:102] INFO: IoU metric:bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.001
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.002
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.015
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.019
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.013
2026-01-20 15:58:12 [det_solver.py:save_best_model:595] INFO: Current metrics: {'coco_eval_bbox': 0.00011287073194746315}
2026-01-20 15:58:12 [det_solver.py:save_best_model:596] INFO: Current avg: 0.0001, Best avg: 0.0001 (epoch 3)
Epoch: 5/400: 100%|██████████| 143/143 [03:02<00:00,  1.28s/batch, d_t=0.0002, it_t=0.2543, memory=2,949 MB, meters=lr: 0.000073  loss: 32.2101 (32.2148)  loss_mal: 1.4853 (1.4652)  loss_bbox: 0.6175 (0.5917)  loss_giou: 1.1843 (1.2138)  loss_fgl: 0.9218 (0.8978)  loss_mal_aux_0: 1.4892 (1.4930)  loss_bbox_aux_0: 0.6019 (0.6019)  loss_giou_aux_0: 1.2043 (1.2286)  loss_fgl_aux_0: 0.9173 (0.8899)  loss_ddf_aux_0: 0.0095 (0.0119)  loss_mal_aux_1: 1.5178 (1.4515)  loss_bbox_aux_1: 0.6164 (0.5919)  loss_giou_aux_1: 1.1876 (1.2168)  loss_fgl_aux_1: 0.9280 (0.8968)  loss_ddf_aux_1: 0.0023 (0.0027)  loss_mal_pre: 1.3658 (1.3078)  loss_bbox_pre: 0.5959 (0.6002)  loss_giou_pre: 1.1998 (1.2309)  loss_mal_enc_0: 1.3161 (1.2551)  loss_bbox_enc_0: 0.6063 (0.6068)  loss_giou_enc_0: 1.2123 (1.2400)  loss_mal_dn_0: 0.7922 (0.7985)  loss_bbox_dn_0: 0.6244 (0.6034)  loss_giou_dn_0: 1.2710 (1.2984)  loss_fgl_dn_0: 0.8663 (0.8575)  loss_ddf_dn_0: 0.0343 (0.0357)  loss_mal_dn_1: 0.8963 (0.9011)  loss_bbox_dn_1: 0.5886 (0.5597)  loss_giou_dn_1: 1.1897 (1.2117)  loss_fgl_dn_1: 0.8948 (0.8812)  loss_ddf_dn_1: 0.0045 (0.0055)  loss_mal_dn_2: 0.9017 (0.9075)  loss_bbox_dn_2: 0.5863 (0.5478)  loss_giou_dn_2: 1.1719 (1.1883)  loss_fgl_dn_2: 0.9015 (0.8864)  loss_mal_dn_pre: 0.8217 (0.8398)  loss_bbox_dn_pre: 0.6236 (0.5991)  loss_giou_dn_pre: 1.2709 (1.2988)]
2026-01-20 16:01:15 [logger.py:log_every:345] INFO: Epoch: 5/400 Total time: 0:03:02 (1.2773 s / it)
2026-01-20 16:01:15 [det_engine.py:train_one_epoch:187] INFO: Averaged stats:lr: 0.000073  loss: 32.2101 (32.2148)  loss_mal: 1.4853 (1.4652)  loss_bbox: 0.6175 (0.5917)  loss_giou: 1.1843 (1.2138)  loss_fgl: 0.9218 (0.8978)  loss_mal_aux_0: 1.4892 (1.4930)  loss_bbox_aux_0: 0.6019 (0.6019)  loss_giou_aux_0: 1.2043 (1.2286)  loss_fgl_aux_0: 0.9173 (0.8899)  loss_ddf_aux_0: 0.0095 (0.0119)  loss_mal_aux_1: 1.5178 (1.4515)  loss_bbox_aux_1: 0.6164 (0.5919)  loss_giou_aux_1: 1.1876 (1.2168)  loss_fgl_aux_1: 0.9280 (0.8968)  loss_ddf_aux_1: 0.0023 (0.0027)  loss_mal_pre: 1.3658 (1.3078)  loss_bbox_pre: 0.5959 (0.6002)  loss_giou_pre: 1.1998 (1.2309)  loss_mal_enc_0: 1.3161 (1.2551)  loss_bbox_enc_0: 0.6063 (0.6068)  loss_giou_enc_0: 1.2123 (1.2400)  loss_mal_dn_0: 0.7922 (0.7985)  loss_bbox_dn_0: 0.6244 (0.6034)  loss_giou_dn_0: 1.2710 (1.2984)  loss_fgl_dn_0: 0.8663 (0.8575)  loss_ddf_dn_0: 0.0343 (0.0357)  loss_mal_dn_1: 0.8963 (0.9011)  loss_bbox_dn_1: 0.5886 (0.5597)  loss_giou_dn_1: 1.1897 (1.2117)  loss_fgl_dn_1: 0.8948 (0.8812)  loss_ddf_dn_1: 0.0045 (0.0055)  loss_mal_dn_2: 0.9017 (0.9075)  loss_bbox_dn_2: 0.5863 (0.5478)  loss_giou_dn_2: 1.1719 (1.1883)  loss_fgl_dn_2: 0.9015 (0.8864)  loss_mal_dn_pre: 0.8217 (0.8398)  loss_bbox_dn_pre: 0.6236 (0.5991)  loss_giou_dn_pre: 1.2709 (1.2988)
Test:: 100%|██████████| 23/23 [00:30<00:00,  1.33s/batch, d_t=0.0004, it_t=0.0747, memory=2,949 MB, meters=]
2026-01-20 16:01:47 [logger.py:log_every:345] INFO: Test: Total time: 0:00:30 (1.3347 s / it)
2026-01-20 16:01:47 [yolo_metrice.py:get_yolo_det_metrice:380] INFO: ------------------------ YOLO Metrics[bbox] Start ------------------------
2026-01-20 16:01:47 [yolo_metrice.py:get_yolo_det_metrice:381] INFO: ------------------------ YOLO指标和COCO指标有差异属于正常情况 ------------------------
Cal YOLO(bbox) mAP...: 100%|██████████| 181/181 [00:00<00:00, 2936.05it/s]
+--------------------------------------------------------------------------+
|                            YOLO Metrics(bbox)                            |
+---------------+-----------+--------+----------+-------+-------+----------+
|    Classes    | Precision | Recall | F1-Score | mAP50 | mAP75 | mAP50-95 |
+---------------+-----------+--------+----------+-------+-------+----------+
|      all      |   0.000   | 0.081  |  0.001   | 0.000 | 0.000 |  0.000   |
|   BackCorner  |   0.000   | 0.075  |  0.000   | 0.000 | 0.000 |  0.000   |
|  FrontCorner  |   0.001   | 0.188  |  0.001   | 0.000 | 0.000 |  0.000   |
| FrontDownBeam |   0.002   | 0.130  |  0.004   | 0.001 | 0.000 |  0.000   |
|    BackBeam   |   0.001   | 0.176  |  0.001   | 0.001 | 0.000 |  0.000   |
|  FrontUpBeam  |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|    BackFoot   |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|   FrontFoot   |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
+---------------+-----------+--------+----------+-------+-------+----------+
2026-01-20 16:01:47 [det_engine.py:evaluate:303] INFO: ------------------------ COCO Metrice Start ------------------------
2026-01-20 16:01:47 [coco_eval.py:summarize:102] INFO: IoU metric:bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.001
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.005
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.020
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.012
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.020
2026-01-20 16:01:47 [det_solver.py:save_best_model:595] INFO: Current metrics: {'coco_eval_bbox': 2.2228047436657725e-05}
2026-01-20 16:01:47 [det_solver.py:save_best_model:596] INFO: Current avg: 0.0000, Best avg: 0.0001 (epoch 3)
Epoch: 6/400: 100%|██████████| 143/143 [03:23<00:00,  1.42s/batch, d_t=0.0020, it_t=0.2638, memory=2,949 MB, meters=lr: 0.000100  loss: 31.0272 (31.8468)  loss_mal: 1.3122 (1.4126)  loss_bbox: 0.5206 (0.5966)  loss_giou: 1.1656 (1.1890)  loss_fgl: 0.9052 (0.9113)  loss_mal_aux_0: 1.2639 (1.4205)  loss_bbox_aux_0: 0.5413 (0.6098)  loss_giou_aux_0: 1.2051 (1.2097)  loss_fgl_aux_0: 0.8968 (0.9016)  loss_ddf_aux_0: 0.0104 (0.0101)  loss_mal_aux_1: 1.2708 (1.4214)  loss_bbox_aux_1: 0.5225 (0.5982)  loss_giou_aux_1: 1.1702 (1.1939)  loss_fgl_aux_1: 0.9067 (0.9095)  loss_ddf_aux_1: 0.0017 (0.0020)  loss_mal_pre: 1.2054 (1.3228)  loss_bbox_pre: 0.5366 (0.6075)  loss_giou_pre: 1.2102 (1.2125)  loss_mal_enc_0: 1.2026 (1.2823)  loss_bbox_enc_0: 0.5442 (0.6158)  loss_giou_enc_0: 1.2363 (1.2289)  loss_mal_dn_0: 0.7866 (0.7746)  loss_bbox_dn_0: 0.5699 (0.5996)  loss_giou_dn_0: 1.2122 (1.2431)  loss_fgl_dn_0: 0.9043 (0.8895)  loss_ddf_dn_0: 0.0459 (0.0482)  loss_mal_dn_1: 0.8548 (0.8633)  loss_bbox_dn_1: 0.5201 (0.5602)  loss_giou_dn_1: 1.1499 (1.1671)  loss_fgl_dn_1: 0.9261 (0.9147)  loss_ddf_dn_1: 0.0067 (0.0075)  loss_mal_dn_2: 0.8798 (0.8787)  loss_bbox_dn_2: 0.5185 (0.5507)  loss_giou_dn_2: 1.1473 (1.1526)  loss_fgl_dn_2: 0.9278 (0.9181)  loss_mal_dn_pre: 0.7753 (0.7824)  loss_bbox_dn_pre: 0.5695 (0.5973)  loss_giou_dn_pre: 1.2135 (1.2435)]
2026-01-20 16:05:10 [logger.py:log_every:345] INFO: Epoch: 6/400 Total time: 0:03:23 (1.4219 s / it)
2026-01-20 16:05:10 [det_engine.py:train_one_epoch:187] INFO: Averaged stats:lr: 0.000100  loss: 31.0272 (31.8468)  loss_mal: 1.3122 (1.4126)  loss_bbox: 0.5206 (0.5966)  loss_giou: 1.1656 (1.1890)  loss_fgl: 0.9052 (0.9113)  loss_mal_aux_0: 1.2639 (1.4205)  loss_bbox_aux_0: 0.5413 (0.6098)  loss_giou_aux_0: 1.2051 (1.2097)  loss_fgl_aux_0: 0.8968 (0.9016)  loss_ddf_aux_0: 0.0104 (0.0101)  loss_mal_aux_1: 1.2708 (1.4214)  loss_bbox_aux_1: 0.5225 (0.5982)  loss_giou_aux_1: 1.1702 (1.1939)  loss_fgl_aux_1: 0.9067 (0.9095)  loss_ddf_aux_1: 0.0017 (0.0020)  loss_mal_pre: 1.2054 (1.3228)  loss_bbox_pre: 0.5366 (0.6075)  loss_giou_pre: 1.2102 (1.2125)  loss_mal_enc_0: 1.2026 (1.2823)  loss_bbox_enc_0: 0.5442 (0.6158)  loss_giou_enc_0: 1.2363 (1.2289)  loss_mal_dn_0: 0.7866 (0.7746)  loss_bbox_dn_0: 0.5699 (0.5996)  loss_giou_dn_0: 1.2122 (1.2431)  loss_fgl_dn_0: 0.9043 (0.8895)  loss_ddf_dn_0: 0.0459 (0.0482)  loss_mal_dn_1: 0.8548 (0.8633)  loss_bbox_dn_1: 0.5201 (0.5602)  loss_giou_dn_1: 1.1499 (1.1671)  loss_fgl_dn_1: 0.9261 (0.9147)  loss_ddf_dn_1: 0.0067 (0.0075)  loss_mal_dn_2: 0.8798 (0.8787)  loss_bbox_dn_2: 0.5185 (0.5507)  loss_giou_dn_2: 1.1473 (1.1526)  loss_fgl_dn_2: 0.9278 (0.9181)  loss_mal_dn_pre: 0.7753 (0.7824)  loss_bbox_dn_pre: 0.5695 (0.5973)  loss_giou_dn_pre: 1.2135 (1.2435)
Test:: 100%|██████████| 23/23 [00:31<00:00,  1.37s/batch, d_t=0.0006, it_t=0.0926, memory=2,949 MB, meters=]
2026-01-20 16:05:43 [logger.py:log_every:345] INFO: Test: Total time: 0:00:31 (1.3715 s / it)
2026-01-20 16:05:43 [yolo_metrice.py:get_yolo_det_metrice:380] INFO: ------------------------ YOLO Metrics[bbox] Start ------------------------
2026-01-20 16:05:43 [yolo_metrice.py:get_yolo_det_metrice:381] INFO: ------------------------ YOLO指标和COCO指标有差异属于正常情况 ------------------------
Cal YOLO(bbox) mAP...: 100%|██████████| 181/181 [00:00<00:00, 1674.70it/s]
+--------------------------------------------------------------------------+
|                            YOLO Metrics(bbox)                            |
+---------------+-----------+--------+----------+-------+-------+----------+
|    Classes    | Precision | Recall | F1-Score | mAP50 | mAP75 | mAP50-95 |
+---------------+-----------+--------+----------+-------+-------+----------+
|      all      |   0.001   | 0.122  |  0.002   | 0.001 | 0.000 |  0.000   |
|   BackCorner  |   0.001   | 0.150  |  0.001   | 0.000 | 0.000 |  0.000   |
|  FrontCorner  |   0.001   | 0.250  |  0.002   | 0.001 | 0.000 |  0.000   |
| FrontDownBeam |   0.000   | 0.056  |  0.001   | 0.000 | 0.000 |  0.000   |
|    BackBeam   |   0.000   | 0.147  |  0.001   | 0.000 | 0.000 |  0.000   |
|  FrontUpBeam  |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|    BackFoot   |   0.002   | 0.222  |  0.005   | 0.007 | 0.000 |  0.003   |
|   FrontFoot   |   0.001   | 0.030  |  0.002   | 0.001 | 0.000 |  0.000   |
+---------------+-----------+--------+----------+-------+-------+----------+
2026-01-20 16:05:43 [det_engine.py:evaluate:303] INFO: ------------------------ COCO Metrice Start ------------------------
2026-01-20 16:05:44 [coco_eval.py:summarize:102] INFO: IoU metric:bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.001
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.003
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.004
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.009
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.030
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.030
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.027
2026-01-20 16:05:44 [det_solver.py:save_best_model:595] INFO: Current metrics: {'coco_eval_bbox': 0.0003782738675932256}
2026-01-20 16:05:44 [det_solver.py:save_best_model:596] INFO: Current avg: 0.0004, Best avg: 0.0004 (epoch 6)
2026-01-20 16:05:44 [det_solver.py:save_best_model:600] INFO: 🎉 New Best Model!
2026-01-20 16:05:44 [det_solver.py:save_best_model:601] INFO:   Epoch: 3 -> 6
2026-01-20 16:05:44 [det_solver.py:save_best_model:602] INFO:   Avg AP: 0.0001 -> 0.0004
2026-01-20 16:05:44 [det_solver.py:save_best_model:608] INFO:   coco_eval_bbox: 0.0001 -> 0.0004
Epoch: 7/400:   0%|          | 0/143 [00:00<?, ?batch/s]2026-01-20 16:05:44 [det_solver.py:save_best_model:618] INFO: 💾 Saved best_stg1.pth
Epoch: 7/400: 100%|██████████| 143/143 [03:16<00:00,  1.38s/batch, d_t=0.0003, it_t=0.2794, memory=2,949 MB, meters=lr: 0.000131  loss: 30.9530 (31.5642)  loss_mal: 1.4705 (1.4075)  loss_bbox: 0.5681 (0.5833)  loss_giou: 1.0573 (1.1571)  loss_fgl: 0.9947 (0.9325)  loss_mal_aux_0: 1.4345 (1.3882)  loss_bbox_aux_0: 0.5697 (0.5952)  loss_giou_aux_0: 1.0870 (1.1745)  loss_fgl_aux_0: 0.9937 (0.9276)  loss_ddf_aux_0: 0.0110 (0.0099)  loss_mal_aux_1: 1.4690 (1.3899)  loss_bbox_aux_1: 0.5690 (0.5838)  loss_giou_aux_1: 1.0580 (1.1599)  loss_fgl_aux_1: 0.9930 (0.9326)  loss_ddf_aux_1: 0.0016 (0.0016)  loss_mal_pre: 1.4206 (1.3555)  loss_bbox_pre: 0.5760 (0.5916)  loss_giou_pre: 1.0914 (1.1766)  loss_mal_enc_0: 1.3944 (1.3387)  loss_bbox_enc_0: 0.5891 (0.6030)  loss_giou_enc_0: 1.1066 (1.1990)  loss_mal_dn_0: 0.7954 (0.7875)  loss_bbox_dn_0: 0.5630 (0.5763)  loss_giou_dn_0: 1.1710 (1.2017)  loss_fgl_dn_0: 0.9294 (0.9143)  loss_ddf_dn_0: 0.0383 (0.0403)  loss_mal_dn_1: 0.8763 (0.8652)  loss_bbox_dn_1: 0.5131 (0.5456)  loss_giou_dn_1: 1.1000 (1.1399)  loss_fgl_dn_1: 0.9571 (0.9358)  loss_ddf_dn_1: 0.0033 (0.0061)  loss_mal_dn_2: 0.8887 (0.8807)  loss_bbox_dn_2: 0.5104 (0.5381)  loss_giou_dn_2: 1.0914 (1.1285)  loss_fgl_dn_2: 0.9607 (0.9389)  loss_mal_dn_pre: 0.7886 (0.7797)  loss_bbox_dn_pre: 0.5611 (0.5751)  loss_giou_dn_pre: 1.1731 (1.2023)]
2026-01-20 16:09:01 [logger.py:log_every:345] INFO: Epoch: 7/400 Total time: 0:03:16 (1.3760 s / it)
2026-01-20 16:09:01 [det_engine.py:train_one_epoch:187] INFO: Averaged stats:lr: 0.000131  loss: 30.9530 (31.5642)  loss_mal: 1.4705 (1.4075)  loss_bbox: 0.5681 (0.5833)  loss_giou: 1.0573 (1.1571)  loss_fgl: 0.9947 (0.9325)  loss_mal_aux_0: 1.4345 (1.3882)  loss_bbox_aux_0: 0.5697 (0.5952)  loss_giou_aux_0: 1.0870 (1.1745)  loss_fgl_aux_0: 0.9937 (0.9276)  loss_ddf_aux_0: 0.0110 (0.0099)  loss_mal_aux_1: 1.4690 (1.3899)  loss_bbox_aux_1: 0.5690 (0.5838)  loss_giou_aux_1: 1.0580 (1.1599)  loss_fgl_aux_1: 0.9930 (0.9326)  loss_ddf_aux_1: 0.0016 (0.0016)  loss_mal_pre: 1.4206 (1.3555)  loss_bbox_pre: 0.5760 (0.5916)  loss_giou_pre: 1.0914 (1.1766)  loss_mal_enc_0: 1.3944 (1.3387)  loss_bbox_enc_0: 0.5891 (0.6030)  loss_giou_enc_0: 1.1066 (1.1990)  loss_mal_dn_0: 0.7954 (0.7875)  loss_bbox_dn_0: 0.5630 (0.5763)  loss_giou_dn_0: 1.1710 (1.2017)  loss_fgl_dn_0: 0.9294 (0.9143)  loss_ddf_dn_0: 0.0383 (0.0403)  loss_mal_dn_1: 0.8763 (0.8652)  loss_bbox_dn_1: 0.5131 (0.5456)  loss_giou_dn_1: 1.1000 (1.1399)  loss_fgl_dn_1: 0.9571 (0.9358)  loss_ddf_dn_1: 0.0033 (0.0061)  loss_mal_dn_2: 0.8887 (0.8807)  loss_bbox_dn_2: 0.5104 (0.5381)  loss_giou_dn_2: 1.0914 (1.1285)  loss_fgl_dn_2: 0.9607 (0.9389)  loss_mal_dn_pre: 0.7886 (0.7797)  loss_bbox_dn_pre: 0.5611 (0.5751)  loss_giou_dn_pre: 1.1731 (1.2023)
Test:: 100%|██████████| 23/23 [00:30<00:00,  1.31s/batch, d_t=0.0003, it_t=0.0888, memory=2,949 MB, meters=]
2026-01-20 16:09:32 [logger.py:log_every:345] INFO: Test: Total time: 0:00:30 (1.3092 s / it)
2026-01-20 16:09:32 [yolo_metrice.py:get_yolo_det_metrice:380] INFO: ------------------------ YOLO Metrics[bbox] Start ------------------------
2026-01-20 16:09:32 [yolo_metrice.py:get_yolo_det_metrice:381] INFO: ------------------------ YOLO指标和COCO指标有差异属于正常情况 ------------------------
Cal YOLO(bbox) mAP...: 100%|██████████| 181/181 [00:00<00:00, 2374.34it/s]
+--------------------------------------------------------------------------+
|                            YOLO Metrics(bbox)                            |
+---------------+-----------+--------+----------+-------+-------+----------+
|    Classes    | Precision | Recall | F1-Score | mAP50 | mAP75 | mAP50-95 |
+---------------+-----------+--------+----------+-------+-------+----------+
|      all      |   0.002   | 0.260  |  0.004   | 0.002 | 0.000 |  0.000   |
|   BackCorner  |   0.001   | 0.550  |  0.003   | 0.001 | 0.000 |  0.000   |
|  FrontCorner  |   0.002   | 0.375  |  0.004   | 0.002 | 0.000 |  0.001   |
| FrontDownBeam |   0.003   | 0.111  |  0.005   | 0.001 | 0.000 |  0.000   |
|    BackBeam   |   0.001   | 0.441  |  0.002   | 0.001 | 0.000 |  0.000   |
|  FrontUpBeam  |   0.000   | 0.000  |  0.000   | 0.000 | 0.000 |  0.000   |
|    BackFoot   |   0.006   | 0.222  |  0.013   | 0.007 | 0.000 |  0.001   |
|   FrontFoot   |   0.002   | 0.121  |  0.003   | 0.003 | 0.000 |  0.001   |
+---------------+-----------+--------+----------+-------+-------+----------+
2026-01-20 16:09:33 [det_engine.py:evaluate:303] INFO: ------------------------ COCO Metrice Start ------------------------
2026-01-20 16:09:33 [coco_eval.py:summarize:102] INFO: IoU metric:bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.002
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.006
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.003
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.019
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.075
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.025
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.075
Epoch: 8/400:   0%|          | 0/143 [00:00<?, ?batch/s]2026-01-20 16:09:33 [det_solver.py:save_best_model:595] INFO: Current metrics: {'coco_eval_bbox': 0.0002934787216065994}
2026-01-20 16:09:33 [det_solver.py:save_best_model:596] INFO: Current avg: 0.0003, Best avg: 0.0004 (epoch 6)
