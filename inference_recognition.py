from set_up import set_up_recognition
from pprint import pprint
from arg_parser.arg_recognition import arg_recognition

def inference_recognition(images_dict, ocr_recognition_model):
    ocr = ocr_recognition_model

    for idx, val in images_dict.items():
        root = val["path"]
        results = list(ocr.predict(input=root))

        images_dict[idx]["label_recognition"] = []

        for res in results:
            rec_texts = res.get("rec_text", [])
            rec_texts = rec_texts.replace(' ', '')

            if not rec_texts:
                images_dict[idx]["label_recognition"].append("not recognize")
            else:
                images_dict[idx]["label_recognition"].append(rec_texts)

    return images_dict

if __name__ == '__main__':
    image_dict = {'image_1': {'object_id': 1, 'label': 'text', 'score': 0.9454976320266724, 'bnd_box': [73, 213, 228, 246], 'path': 'dataset/checking_dataset/text_detection_result\\cropped_image_1_text.png'}, 'image_2': {'object_id': 2, 'label': 'text', 'score': 0.9453274607658386, 'bnd_box': [110, 106, 285, 139], 'path': 'dataset/checking_dataset/text_detection_result\\cropped_image_2_text.png'}, 'image_3': {'object_id': 3, 'label': 'text', 'score': 0.9417890906333923, 'bnd_box': [104, 365, 200, 401], 'path': 'dataset/checking_dataset/text_detection_result\\cropped_image_3_text.png'}}
    args = arg_recognition()
    ocr_model = set_up_recognition(args)
    recognition = inference_recognition(image_dict, ocr_model)
    pprint(recognition)