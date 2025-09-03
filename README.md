Text Translation with Deep Learning models

This project is about creating AI, allowing to detect and recognize texts from user captured image to translate them to another language.

- Dataset: Total Text - Scene Text Recognition (Kaggle)
- Dataset link: https://www.kaggle.com/datasets/ipythonx/totaltextstr
- Detection: YOLOv11
- Recognition: Paddle OCR
- Translate: Argo Translate  

HOW IT WORK ?
<img width="1074" height="211" alt="image" src="https://github.com/user-attachments/assets/ab439a04-8770-4399-8c30-53787c558efb" />  


HOW TO USE ?  
A. Install requirement from requirement.txt  
   Note:  
   - The system need to have trained model to run. To train model follow B part (below).  
   - To run AI models in training and inference, I recommend using GPU by install cuda  

B. For trainning:  
   1. Run yolo_processing:  
      <img width="345" height="43" alt="image" src="https://github.com/user-attachments/assets/29862266-1766-407e-a1f5-4bebf6bcdd75" />  
         - When running yolo_processing.py, the system will create dataset folder for containing text_dataset folder
         - text_dataset folder will contain yolo structure dataset, include images and annotations (txt files) for both Train and Test set   
           <img width="295" height="161" alt="image" src="https://github.com/user-attachments/assets/83d6ed3f-620b-4305-920a-f4c4c52b34a9" />  
   2. Prepare data.yaml: In path, replace with your dataset directory  
      Note: dataset folder need to follow YOLOv5 dataset structure  
   3. Train YOLO model with data.yaml  
      - For new model:  
      <img width="278" height="28" alt="image" src="https://github.com/user-attachments/assets/969ccad2-aae5-4ebf-8b18-a64c57fdfd45" />
  
      - For pre-trained model:  
      <img width="705" height="31" alt="image" src="https://github.com/user-attachments/assets/16539915-82b2-42f3-92b8-683adb02652f" />

         + pre_train: set True system will pre-train model and vice versa  
         + model_pretrain_dir: model use for pre-train   

 

C. For running:
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


