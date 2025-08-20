import argparse

def arg_translation():
    parser = argparse.ArgumentParser(
        prog="Translation",
        description="Manage inference_translation, use for translate recognize text in image/cropped image"
    )

    parser.add_argument("--model_translation", type=str,
                        default="dataset/language_dataset/translate-en_vi-1_0.argosmodel",
                        help="downloaded model path (argostranslate package)")
    parser.add_argument("--from_code", type=str, default="en", help="language will be translated")
    parser.add_argument("--to_code", type=str, default="vi", help="language use for translate")
    parser.add_argument("--downloaded_package", type=bool, default=False,
                        help="True: use downloaded model - False: use online model")
    parser.add_argument("--show_translation_result", type=bool, default=False, help="Show translate result")

    args = parser.parse_args()
    return args