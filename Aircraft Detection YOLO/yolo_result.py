from ultralytics import YOLO

"""
run predictions saved model using our own weights
"""
model = YOLO("C:/Users/Admin/Desktop/RS OEA/runs/detect/train2/weights/best.pt")

#predict results
results = model.predict("C:/Users/Admin/Desktop/RS OEA/data/test", save=True,conf=0.5)

metrics = model.val()  # no arguments needed, dataset and settings remembered
print(metrics.box.map)   # map50-95
print(metrics.box.map50)