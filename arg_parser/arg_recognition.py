import argparse

def arg_recognition():
    parser = argparse.ArgumentParser(
        prog="Recognition",
        description="Manage inference_recognition, use for recognite text in image/cropped image"
    )

    parser.add_argument("--model_recognition", type=str, default="PP-OCRv5_server_rec", help="Paddle OCR model name")
    parser.add_argument("--language_recognition", type=str, default=None, help="language for recognition")

    args = parser.parse_args([])
    return args