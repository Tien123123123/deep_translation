import argparse

def arg_train():
    parser = argparse.ArgumentParser(
        prog="Detection",
        description="Manage train.py, use for training YOLO model"
    )

    parser.add_argument("-m", "--model", type=str, default="yolo11n.pt", help="yolo model")
    parser.add_argument("-p", "--pre_train", type=bool, default=False, help="pre-train yolo model")
    parser.add_argument("--model_pretrain_dir", type=str, default="run/detect/train/weights/best.pt", help="pre-train model path")
    parser.add_argument("-d", "--data", type=str, default=f"data.yaml", help="file yaml for yolo to get data")

    args = parser.parse_args()
    return args

