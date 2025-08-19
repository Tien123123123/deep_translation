import os
import cv2
import warnings
from pprint import pprint
from arg_parser.arg_detection import arg_detection
from set_up import set_up_models
warnings.filterwarnings("ignore", category=FutureWarning)

def inference_detection(yolo_model):
    arg = arg_detection()
    item = arg.img_dir

    model = yolo_model
    model.eval()

    predictions = model(item)
    # predictions.show()
    preds = predictions.xyxy[0]

    # Inference
    image = cv2.imread(item)
    inf_images = {}
    show_object_detection = arg.show_object
    show_detection_result = arg.result
    thresh_hold = 0.5

    for idx, pred in enumerate(preds):
        xmin, ymin, xmax, ymax, conf_thresh, cls = pred
        xmin, ymin, xmax, ymax, conf_thresh, cls = int(xmin), int(ymin), int(xmax), int(ymax), float(conf_thresh), int(cls)

        if conf_thresh < thresh_hold:
            continue

        label = model.names[int(cls)]
        if show_object_detection == True:
            print("--"*50)
            print(f"Object {idx + 1}")
            print(f"Label: {label}, Confidence: {conf_thresh:.3f}")
            print(f"Bounding Box: [x_min: {xmin:.1f}, y_min: {ymin:.1f}, x_max: {xmax:.1f}, y_max: {ymax:.1f}]")

        if show_detection_result == True:
            cv2_image = cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
            cv2.putText(cv2_image, f"{label}-{conf_thresh:.3f}", (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cropped_image = image[ymin:ymax, xmin:xmax]
        output_path = os.path.join(arg.out_path, f"cropped_image_{idx + 1}_{label}.png")
        cv2.imwrite(output_path, cropped_image)
        if show_object_detection == True:
            print("--" * 50)
            if os.path.exists(output_path):
                print(f"Cropped image saved to {output_path}")
            else:
                print(f"Cannot crop Image {idx + 1}")
                print(f"Bounding Box: [x_min: {xmin:.1f}, y_min: {ymin:.1f}, x_max: {xmax:.1f}, y_max: {ymax:.1f}]")

        inf_images[f"image_{idx + 1}"] = {
            "object_id": idx + 1,
            "label": label,
            "score": conf_thresh,
            "bnd_box": [xmin, ymin, xmax, ymax],
            "path": output_path
        }

    if show_detection_result == True:
        cv2.imshow("Detection result - Close to continue process", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return inf_images

if __name__ == '__main__':
    yolo_model, ocr_model = set_up_models()
    detection = inference_detection(yolo_model)
    pprint(detection)