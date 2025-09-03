from ultralytics import YOLO
from arg_parser.arg_train import arg_train

def train(args):
    pre_train = args.pre_train
    if pre_train != True:
        print("Prepare to train")
        model_root = "yolo11n.pt"
    else:
        print("Prepare to pre-train")
        model_root = f"run/detect/train/weights/best.pt"

    model = YOLO(model_root)

    results = model.train(
        data="data.yaml",
        epochs=100,
        imgsz=640,
        device=0
    )

if __name__ == '__main__':
    args = arg_train()
    train(args)