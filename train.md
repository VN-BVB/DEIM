--train--
CUDA_VISIBLE_DEVICES=0 torchrun --master_port=7777 --nproc_per_node=1 train.py -c deim_hgnetv2_n_test.yml --seed=0 -t deim_dfine_hgnetv2_s_coco_120e.pth
--test--
CUDA_VISIBLE_DEVICES=0 torchrun --master_port=7777 --nproc_per_node=1 train.py -c deim_hgnetv2_n_test.yml --test--only -r deim_dfine_hgnetv2_s_coco_120e.pth
通过修改yml中的val地址来修改
--
tensorboard --logdir=/ summary中的文件