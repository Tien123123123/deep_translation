import os, cv2
import numpy as np
from inference_detection import inference_detection
from inference_recognition import inference_recognition
from inference_translate import inference_translate
from data_processing.connect_bndbox import cal_bndbox
from PIL import Image, ImageDraw, ImageFont
from data_processing.text_processing import seperate_word, flatten_and_convert
from arg_parser.arg_detection import arg_detection
from set_up import set_up_inference, set_up_models

def put_text(images_dict, args):
    ori_image = f"{args.img_dir}"
    image = cv2.imread(ori_image)
    for idx, val in images_dict.items():
        if val["label_recognition"][0] != "not recognize":
            xmin, ymin, xmax, ymax = val["bnd_box"]

            fontpath = "./arial.ttf"
            font = ImageFont.truetype(fontpath, 20)
            img_pil = Image.fromarray(image)
            draw = ImageDraw.Draw(img_pil)
            draw.text((xmin, ymin - 30),f"{" ".join(val["label_recognition"])}", font=font, fill=(0, 255, 0, 0))
            image = np.array(img_pil)

    output_image = f"dataset/checking_dataset/output_image.jpg"
    cv2.imwrite(output_image, image)
    if os.path.exists(output_image):
        print(f"Image save successfully at {output_image}")
    else:
        print(f"Cannot save Image to {output_image}")

    cv2.imshow("result", image)
    cv2.waitKey()
    cv2.destroyAllWindows()


def inference(args):
    args_detect = args
    print("Set up models and resources for inference...")
    yolo_model, ocr_model = set_up_models(args_detect)
    set_up_inference()

    print("Text detection processing...")
    images_dict = inference_detection(yolo_model, args_detect)

    print("Text recognition processing...")
    images_dict = inference_recognition(images_dict, ocr_model)
    data_dict = cal_bndbox(images_dict)

    print("Text translation processing...")
    for key, val in data_dict.items():
        label = val["label_recognition"]
        label = label.replace('-', ' ')
        if " " not in label or str(label).isalpha():
            label = inference_translate(label)
        else:
            label = seperate_word(label)
            label = flatten_and_convert(label)
        data_dict[key] = {
            'bnd_box': val['bnd_box'],
            'label_recognition': label
        }

    put_text(data_dict, args_detect)

if __name__ == '__main__':
    args = arg_detection()
    inference(args)