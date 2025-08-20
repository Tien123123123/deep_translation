import argparse

def arg_translation():
    parser = argparse.ArgumentParser(
        prog="Translation",
        description="Manage inference_translation, use for translate recognize text in image/cropped image"
    )

    parser.add_argument("-m", "--model", type=str, default="dataset/language_dataset/translate-en_vi-1_0.argosmodel", help="downloaded model path (argostranslate package)")
    parser.add_argument("-f", "--from_code", type=str, default="en", help="language will be translated")
    parser.add_argument("-t", "--to_code", type=str, default="vi", help="language use for translate")

    parser.add_argument("-s", "--show_result", type=bool, default= False, help="Show translate result")

    args = parser.parse_args([])
    return args