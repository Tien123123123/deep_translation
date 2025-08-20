import os, shutil
import torch
from paddleocr import TextRecognition

def set_up_detection(args):
    yolo_root = args.yolo_dir
    exp_root = os.path.join(yolo_root, f"runs/train/{args.exp}/weights/best.pt")
    model_yolo = torch.hub.load(yolo_root, "custom", exp_root, source="local")

    return model_yolo

def set_up_recognition(args):
    model_ocr = TextRecognition(
        model_name=args.model_recognition
    )

    return model_ocr

def set_up_models(args):
    detection = set_up_detection(args)
    recognition = set_up_recognition(args)

    return detection, recognition

def set_up_inference():
    root = "dataset/"
    checking_dataset_root = os.path.join(root, "checking_dataset")
    detection_result = os.path.join(checking_dataset_root, "text_detection_result")

    if os.path.exists(detection_result):
        shutil.rmtree(detection_result)
    os.makedirs(detection_result)

def set_up_translation():
    root = "../dataset/language_dataset"

    if not os.path.exists(root):
        os.makedirs(root)
        print(f"Create {root} successfully!")
    print(f"{root} exists")

if __name__ == '__main__':
    set_up_inference()
    set_up_translation()