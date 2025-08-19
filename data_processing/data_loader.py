import os
import shutil
import kagglehub
import cv2
import re

class customized_data():
    def __init__(self):
        path = kagglehub.dataset_download("ipythonx/totaltextstr")
        self.root = os.path.join(path, "Total-Text")
        self.data_pth = []

        with os.scandir(self.root) as dir:
            for item in dir:
                self.data_pth.append(item.path)

    def min_max_capture(self, item):
        # Extract all numbers from the item using regex
        numbers = re.findall(r'\d+', item)
        array = [int(x) for x in numbers if x]
        return min(array), max(array)

    def target_bndbox(self, txt_file):
        target_list = []
        print(f"txt file: {txt_file}", end="\r")
        with open(txt_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            current_line = ""
            for line in lines:
                line = line.strip()
                if not line:  # Bỏ qua các dòng trống
                    continue
                # Nếu dòng không kết thúc bằng ']', nối vào current_line
                if not line.endswith(']'):
                    current_line += " " + line
                    continue
                else:
                    current_line += " " + line
                    # Chuẩn hóa current_line: thay thế nhiều khoảng trắng hoặc xuống dòng bằng một khoảng trắng
                    current_line = re.sub(r'\s+', ' ', current_line.strip())
                    if "ornt: [u'#']" in current_line:
                        current_line = ""
                        continue

                    # Tách dòng đã nối bằng dấu phẩy
                    items = current_line.split(", ")
                    xmin, xmax, ymin, ymax = None, None, None, None

                    for item in items:
                        if "x:" in item:
                            item = item.replace("x: ", "").strip()
                            xmin, xmax = self.min_max_capture(item)
                        elif "y:" in item:
                            item = item.replace("y: ", "").strip()
                            ymin, ymax = self.min_max_capture(item)

                    if all(v is not None for v in [xmin, ymin, xmax, ymax]):
                        target_list.append([xmin, ymin, xmax, ymax])
                    current_line = ""  # Đặt lại cho object tiếp theo

        print(f"target list: {target_list}", end="\r")
        return target_list

    def get_image_size(self, data_pth, file_name="train", image_id="img1001"):
        for pth in data_pth:
            if pth.lower().endswith(file_name):
                with os.scandir(pth) as dir:
                    for item in dir:
                        if image_id.split(".")[0] in item.name:
                            ori_image = cv2.imread(item)
                            image = cv2.cvtColor(ori_image, cv2.COLOR_BGR2RGB)
                            height, width = image.shape[:2]
                            return height, width


if __name__ == '__main__':
    pass