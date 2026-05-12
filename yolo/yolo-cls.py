from ultralytics import YOLO
import sys
print(sys.version)

model = YOLO('yolov8n-cls.pt')
model.verbose = True
finned = model.train(data='splited', epochs=100, imgsz=224, verbose=True)