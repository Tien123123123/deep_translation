import sys, os, re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from argostranslate import package, translate
from arg_parser.arg_translation import arg_translation

def inference_translate(data):
    arg = arg_translation()
    # receive text
    str_list = data

    # install language
    root = arg.model
    from_code = arg.from_code
    to_code = arg.to_code
    downloaded_package = True
    if os.path.exists(root) and downloaded_package:
        package.install_from_path(root)
    else:
        package.update_package_index()
        available_packages = package.get_available_packages()
        package_to_install = next(
            filter(
                lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
            )
        )
        package.install_from_path(package_to_install.download())

    # translate
    str_item = str(str_list).lower()
    is_valid = bool(re.match(r'^[a-zA-Z0-9\s\'\-]*$', str_item, re.UNICODE))
    if is_valid:
        str_item = translate.translate(str_item, from_code, to_code)
    else:
        return str_item

    if arg.show_result == True:
        print("--" * 10)
        print(f"Before: {str_list}")
        print(f"After: {str_item}")

    return str_item


if __name__ == '__main__':
    data = {'object_1': {'bnd_box': [145, 84, 518, 107],
              'label_recognition': "Beef Stir Fry"},
 'object_2': {'bnd_box': [75, 274, 580, 320],
              'label_recognition': 'Restaurant INC'},
 'object_3': {'bnd_box': [264, 337, 394, 385], 'label_recognition': '1918'},
 'object_4': {'bnd_box': [206, 862, 465, 894],
              'label_recognition': 'George Jean Nathan'}}

    for key, val in data.items():
        translated_str = inference_translate(val["label_recognition"])
        data[key]["label_recognition"] = translated_str

    print(data)