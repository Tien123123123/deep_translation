import argparse

def arg_inference():
    parser = argparse.ArgumentParser(
        prog="Inference",
        description="Manage inference, use for detect, recognize and translate texts in image"
    )

    # detection
    parser.add_argument("--yolo_dir", type=str, default="../../yolov5", help="yolo path")
    parser.add_argument("--exp", type=str, default="exp29", help="yolo exp")
    parser.add_argument("--img_dir", type=str, default="dataset/checking_dataset/image.jpg", help="image path")
    parser.add_argument("--out_path", type=str, default=f"dataset/checking_dataset/text_detection_result")
    parser.add_argument("-t", "--thresh_hold", type=float, default=0.5, help="thresh hold for detection")
    parser.add_argument("--show_detection_object", type=bool, default=False, help="show detected objects")
    parser.add_argument("--show_detection_result", type=bool, default=False, help="show detection result")

    # recognition
    parser.add_argument("--model_recognition", type=str, default="PP-OCRv5_server_rec", help="Paddle OCR model name")
    parser.add_argument("--language_recognition", type=str, default=None, help="language for recognition")

    # translation
    parser.add_argument("--model_translation", type=str, default="dataset/language_dataset/translate-en_vi-1_0.argosmodel",
                        help="downloaded model path (argostranslate package)")
    parser.add_argument("--from_code", type=str, default="en", help="language will be translated")
    parser.add_argument("--to_code", type=str, default="vi", help="language use for translate")
    parser.add_argument("--downloaded_package", type=bool, default=False,
                        help="True: use downloaded model - False: use online model")
    parser.add_argument("--show_translation_result", type=bool, default=False, help="Show translate result")

    args = parser.parse_args()
    return args

