import os
import json
from PIL import Image, ImageFile
from tqdm import tqdm
from datetime import datetime

ImageFile.LOAD_TRUNCATED_IMAGES = True

YOLO_ROOT = "YOLO_Format"
IMAGE_ROOT = os.path.join(YOLO_ROOT, "images")
LABEL_ROOT = os.path.join(YOLO_ROOT, "labels")
ANNOTATION_ROOT = os.path.join(YOLO_ROOT, "annotations")
LABEL_TXT = os.path.join(YOLO_ROOT, "labels.txt")

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"}


def load_classes(label_txt_path):
    classes = []
    with open(label_txt_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            classes.append(parts[1])
    return classes


def find_image(label_file, image_dir):
    base = os.path.splitext(label_file)[0]
    for ext in IMAGE_EXTS:
        img_path = os.path.join(image_dir, base + ext)
        if os.path.exists(img_path):
            return img_path
    return None


def polygon_area(points):
    area = 0.0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0


def polygon_bbox(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    return [x_min, y_min, x_max - x_min, y_max - y_min]


def build_base_coco(classes):
    now = datetime.utcnow().isoformat() + "+00:00"

    return {
        "info": {
            "year": "2025",
            "version": "1.0",
            "description": "Converted from YOLO segmentation format",
            "contributor": "",
            "url": "",
            "date_created": now
        },
        "licenses": [
            {
                "id": 1,
                "url": "https://creativecommons.org/licenses/by/4.0/",
                "name": "CC BY 4.0"
            }
        ],
        "categories": [
            {
                "id": i,
                "name": name,
                "supercategory": name
            }
            for i, name in enumerate(classes)
        ],
        "images": [],
        "annotations": []
    }


def convert_split(split, classes):
    image_dir = os.path.join(IMAGE_ROOT, split)
    label_dir = os.path.join(LABEL_ROOT, split)

    coco = build_base_coco(classes)

    image_id = 0
    ann_id = 0

    label_files = [f for f in os.listdir(label_dir) if f.endswith(".txt")]

    for label_file in tqdm(label_files, desc=f"Converting {split}", ncols=100):
        image_path = find_image(label_file, image_dir)
        if image_path is None:
            continue

        with Image.open(image_path) as img:
            width, height = img.size

        file_name = os.path.basename(image_path)

        coco["images"].append({
            "id": image_id,
            "license": 1,
            "file_name": file_name,
            "height": height,
            "width": width,
            "date_captured": coco["info"]["date_created"],
            "extra": {
                "name": os.path.splitext(file_name)[0]
            }
        })

        with open(os.path.join(label_dir, label_file), "r") as f:
            lines = f.readlines()

        for line in lines:
            parts = line.strip().split()
            if len(parts) < 7:
                continue

            class_id = int(parts[0])
            coords = list(map(float, parts[1:]))

            polygon = []
            for i in range(0, len(coords), 2):
                polygon.append([
                    coords[i] * width,
                    coords[i + 1] * height
                ])

            area = polygon_area(polygon)
            bbox = polygon_bbox(polygon)

            coco["annotations"].append({
                "id": ann_id,
                "image_id": image_id,
                "category_id": class_id,
                "bbox": bbox,
                "area": area,
                "segmentation": [[v for p in polygon for v in p]],
                "iscrowd": 0
            })

            ann_id += 1

        image_id += 1

    return coco


def main():
    os.makedirs(ANNOTATION_ROOT, exist_ok=True)

    classes = load_classes(LABEL_TXT)

    for split in ["train", "val", "test"]:
        coco_data = convert_split(split, classes)
        out_path = os.path.join(ANNOTATION_ROOT, f"{split}.json")

        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(coco_data, f, ensure_ascii=False, indent=2)

        print(f"[OK] Saved: {out_path}")


if __name__ == "__main__":
    main()
