import os
import cv2
import json
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import argparse


# ====================== 配置区（一般不用改） ======================
ROOT_DIR = "YOLO_Format"      # 数据集根目录
PHASES = ["train", "val", "test"]
IMAGE_EXTS = [".jpg", ".png", ".bmp"]
# =================================================================


def load_classes(label_path):
    """
    label.txt format:
    id class_name R G B
    """
    classes = []

    with open(label_path, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) < 2:
                print(f"[WARN] Invalid label line {line_no}: {line}")
                continue

            class_name = parts[1]
            classes.append(class_name)

    if not classes:
        raise ValueError("No valid classes found in label.txt")

    return classes



def yolo_to_coco_single_phase(root_dir, phase, classes):
    images_dir = os.path.join(root_dir, "images", phase)
    labels_dir = os.path.join(root_dir, "labels", phase)
    save_dir = os.path.join(root_dir, "annotations")
    os.makedirs(save_dir, exist_ok=True)

    coco = {
        "images": [],
        "annotations": [],
        "categories": []
    }

    # categories
    for i, name in enumerate(classes):
        coco["categories"].append({
            "id": i,
            "name": name,
            "supercategory": "object"
        })

    image_files = sorted([
        f for f in os.listdir(images_dir)
        if os.path.splitext(f)[1].lower() in IMAGE_EXTS
    ])

    ann_id = 0

    print(f"\n[INFO] Processing {phase} set: {len(image_files)} images")

    for img_id, img_name in enumerate(tqdm(image_files)):
        img_path = os.path.join(images_dir, img_name)
        label_path = os.path.join(
            labels_dir,
            os.path.splitext(img_name)[0] + ".txt"
        )

        img = cv2.imread(img_path)
        if img is None:
            print(f"[WARNING] Cannot read image: {img_path}")
            continue

        h, w = img.shape[:2]

        coco["images"].append({
            "id": img_id,
            "file_name": f"{phase}/{img_name}",
            "width": w,
            "height": h
        })

        if not os.path.exists(label_path):
            continue

        with open(label_path, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 5:
                    continue

                cls_id, x, y, bw, bh = map(float, parts)

                # YOLO -> COCO
                x1 = (x - bw / 2) * w
                y1 = (y - bh / 2) * h
                bw = bw * w
                bh = bh * h

                coco["annotations"].append({
                    "id": ann_id,
                    "image_id": img_id,
                    "category_id": int(cls_id),
                    "bbox": [
                        round(x1, 2),
                        round(y1, 2),
                        round(bw, 2),
                        round(bh, 2)
                    ],
                    "area": round(bw * bh, 2),
                    "iscrowd": 0,
                    "segmentation": [[
                        x1, y1,
                        x1 + bw, y1,
                        x1 + bw, y1 + bh,
                        x1, y1 + bh
                    ]]
                })

                ann_id += 1

    save_path = os.path.join(save_dir, f"{phase}.json")
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(coco, f, ensure_ascii=False, indent=2)

    print(f"[OK] Saved {phase}.json -> {save_path}")


def main():
    print("========== YOLO → COCO Converter ==========")

    label_path = os.path.join(ROOT_DIR, "label.txt")
    if not os.path.exists(label_path):
        raise FileNotFoundError("label.txt not found")

    classes = load_classes(label_path)
    print(f"[INFO] Loaded {len(classes)} classes")

    for phase in PHASES:
        img_dir = os.path.join(ROOT_DIR, "images", phase)
        lbl_dir = os.path.join(ROOT_DIR, "labels", phase)

        if not os.path.exists(img_dir) or not os.path.exists(lbl_dir):
            print(f"[SKIP] {phase} not found")
            continue

        yolo_to_coco_single_phase(ROOT_DIR, phase, classes)

    print("\n🎉 All done!")


if __name__ == "__main__":
    main()
