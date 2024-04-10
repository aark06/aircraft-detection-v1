# !pip install ultralytics
# !yolo train model=yolov8s.pt data="/kaggle/working/data.yaml" epochs=10
# import ultralytics
# ultralytics.checks()

from ultralytics import YOLO

# Load a model
model = YOLO("yolov8s.yaml")  # build a new model from scratch
model = YOLO("yolov8s.pt")

""" 
model train on our yaml file
"""
model.train(data="C:/Users/Admin/Desktop/RS OEA/yolo_config.yaml", epochs=10, patience=3)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
path = model.export(format="onnx")

