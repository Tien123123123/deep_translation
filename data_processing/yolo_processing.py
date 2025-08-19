import os, sys, cv2
import shutil
from data_loader import customized_data

class yolo_dataset(customized_data):
    def __init__(self):
        super().__init__()
        self.annotation_type = "groundtruth_polygonal_annotation"

    def create_yolo_folder(self):
        yolo_dataset_pth = "../dataset/text_dataset"

        dataset_type = ["images", "labels"]
        children = ["train", "test"]

        if os.path.isdir(yolo_dataset_pth):
            print(f"Found old directory {yolo_dataset_pth}")
            shutil.rmtree(yolo_dataset_pth)
            print(f"Removed old directory!")
        os.makedirs(yolo_dataset_pth)

        for type in dataset_type:
            parent_root = os.path.join(yolo_dataset_pth, type)
            os.makedirs(parent_root)
            for child in children:
                os.makedirs(os.path.join(parent_root, child))

        if yolo_dataset_pth:
            print(f"Yolo dataset is created successfully at {yolo_dataset_pth}")

    def yolo_calculation(self, target_list, height, width):
        annotations = []
        for target in target_list:
            image_h, image_w = height, width
            xmin, ymin, xmax, ymax = target

            xcent = (xmin + xmax) / 2
            ycent = (ymin + ymax) / 2

            bndw = xmax - xmin
            bndh = ymax - ymin

            # Norm
            xnorm = xcent / image_w
            ynorm = ycent / image_h

            wnorm = bndw / image_w
            hnorm = bndh / image_h

            annotations.append([xnorm, ynorm, wnorm, hnorm])
        return annotations

    def yolo_insert_data_to_txt(self, annotaions, image_id, file_name, label=0):
        root = f"../dataset/text_dataset/labels/{file_name}"
        txt_file = f"{image_id}.txt"

        file_root = os.path.join(root, txt_file)
        with open(file_root, "w") as f:
            for annotaion in annotaions:
                xnorm, ynorm, wnorm, hnorm = annotaion
                f.write(f"{label} {xnorm} {ynorm} {wnorm} {hnorm}\n")

    def annotation_loader(self, file_name="train"):
        for pth in self.data_pth:
            if pth.lower().endswith("annotation"):
                anno_dir = os.path.join(pth, f"{self.annotation_type}/{file_name}")

                with os.scandir(anno_dir) as dir:
                    for item in dir:
                        anno_name = item.name.split("_")[2]
                        height, width = self.get_image_size(self.data_pth, file_name, anno_name)
                        target_list = self.target_bndbox(item.path)
                        annotations = self.yolo_calculation(target_list, height, width)
                        self.yolo_insert_data_to_txt(annotations, anno_name.split(".")[0], file_name)

    def image_loader(self, file_name="train"):
        for pth in self.data_pth:
            if pth.lower().endswith(file_name):
                with os.scandir(pth) as dir:
                    for item in dir:
                        image_name = item.name.split(".")[0]
                        yolo_image_pth = f"../dataset/text_dataset/images/{file_name}/{image_name}.jpg"
                        shutil.copy(item.path, yolo_image_pth)

if __name__ == '__main__':

    dataset = yolo_dataset()
    dataset.create_yolo_folder()

    print("-"*10)
    dataset.image_loader(file_name="train")
    dataset.annotation_loader(file_name="train")
    print("Train type--")
    print("-" * 10)
    dataset.image_loader(file_name="test")
    dataset.annotation_loader(file_name="test")
    print("Test type--")
    print("-" * 10)
