def cal_bndbox(data_dict, thresh_hold=30):
    used = []
    data = data_dict
    thresh_hold = thresh_hold
    lines = []
    for key, val in data.items():
        if key in used:
            continue
        used.append(key)
        current_line = [
            {
                "label_recognition": val["label_recognition"],
                "bnd_box": val["bnd_box"]
            }
        ]
        ymin, ymax = val["bnd_box"][1], val["bnd_box"][3]
        for key_2, val_2 in data.items():
            if key_2 in used or key_2 == key:
                continue

            ymin_2, ymax_2 = val_2["bnd_box"][1], val_2["bnd_box"][3]

            if abs(ymin - ymin_2) <= thresh_hold and abs(ymax - ymax_2) < thresh_hold:
                current_line.append({
                    "label_recognition": val_2["label_recognition"],
                    "bnd_box": val_2["bnd_box"]
                })
                used.append(key_2)
        current_line.sort(key=lambda x: x["bnd_box"][0])
        lines.append(current_line)
    lines.sort(key=lambda x: x[0]["bnd_box"][1])

    sorted_dict = {}
    idx = 0
    x_mins, y_mins, x_maxs, y_maxs = [], [], [], []

    for line in lines:
        x_mins, y_mins, x_maxs, y_maxs = [], [], [], []
        valid_labels = [item["label_recognition"][0] for item in line if
                        item["label_recognition"][0] != "not recognize"]

        if not valid_labels:
            continue

        for item in line:
            x_min, y_min, x_max, y_max = item["bnd_box"]
            x_mins.append(x_min)
            y_mins.append(y_min)
            x_maxs.append(x_max)
            y_maxs.append(y_max)

        sorted_dict[f"object_{idx + 1}"] = {
            "label_recognition": " ".join(valid_labels),
            "bnd_box": [min(x_mins), min(y_mins), max(x_maxs), max(y_maxs)]
        }
        idx += 1

    return sorted_dict
