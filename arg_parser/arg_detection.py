import argparse

def arg_detection():
    parser = argparse.ArgumentParser(
        prog="Detection",
        description="Manage inference_detection, use for detect text in image"
    )

    parser.add_argument("-y", "--yolo_dir", type=str, default="../../yolov5", help="yolo path")
    parser.add_argument("-e", "--exp", type=str, default="exp29", help="yolo exp")
    parser.add_argument("-i", "--img_dir", type=str, default="dataset/checking_dataset/image.jpg", help="image path")
    parser.add_argument("-o", "--out_path", type=str, default=f"dataset/checking_dataset/text_detection_result")

    parser.add_argument("-s", "--show_object", type=bool, default=False, help="show detected objects")
    parser.add_argument("-r", "--result", type=bool, default=False, help="show detection result")

    args = parser.parse_args()
    return args

