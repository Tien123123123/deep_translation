Text Translation with Deep Learning models

This project is about creating AI, allowing to detect and recognize texts from user captured image to translate them to another language.

- Dataset: Total Text - Scene Text Recognition (Kaggle)
- Dataset link: https://www.kaggle.com/datasets/ipythonx/totaltextstr
- Detection: YOLOv5
- Recognition: Paddle OCR
- Translate: Argo Translate

HOW IT WORK ?
<img width="1074" height="211" alt="image" src="https://github.com/user-attachments/assets/ab439a04-8770-4399-8c30-53787c558efb" />



HOW TO USE ?
1. Install requirement from requirement.txt

2. For training
...
3. For running:
   1. Run set_up.py: when running set_up.py, system will create dataset folder for containing checking_dataset and language_dataset
      <img width="314" height="67" alt="image" src="https://github.com/user-attachments/assets/9f2d1ba5-09b5-4599-a2f8-fca9cf20d6b3" />
         - checking_dataset:
              + Input image: image use for inference
              + Output image: translated image
              + text_detection_result: contain cropped images from detection model, use for recognition later
                <img width="254" height="140" alt="image" src="https://github.com/user-attachments/assets/7320f4be-231d-4ec4-b16a-474c6f206b56" />

         - language_dataset: contain Argo Translate downloaded models
           <img width="278" height="47" alt="image" src="https://github.com/user-attachments/assets/e0c5638a-d555-4d66-a256-9c0d4e77ab05" />

   2. Run inference.py
      - Quick CLI: <img width="521" height="30" alt="image" src="https://github.com/user-attachments/assets/50d8b70e-caa3-4fba-8a75-82dac7b2a6af" />
      
      - CLI with translate: <img width="940" height="29" alt="image" src="https://github.com/user-attachments/assets/4cc8f70b-0bf6-44f5-ac35-a9ad27439c66" />

         + img_dir: input image directory
         + from_code: original language
         + to_code: language to translate
         + download_package: True if having download model in "language dataset" folder else False
           * Note: translate language package need to be in Argos Translate Package Index. If not, try download package and put it in "language_dataset" folder
           * Argos Translate Package Index: https://www.argosopentech.com/argospm/index
  
RESULT:
- Detection
   <img width="447" height="273" alt="image" src="https://github.com/user-attachments/assets/d0357571-9adf-46e4-831c-ab9fb7b5977e" />

- Translation:
   <img width="447" height="266" alt="image" src="https://github.com/user-attachments/assets/6adc2ace-1fe2-4535-bb9f-5f5626565624" />


