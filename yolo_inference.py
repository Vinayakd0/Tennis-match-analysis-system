from ultralytics import YOLO

# Load the YOLOv8x model
# model = YOLO(r'C:\Users\admin\Desktop\Tennis-analysis-system\model\best.pt')
model = YOLO('yolov8x')
result= model.track('input_videos/input_video.mp4',conf=0.2, save=True)
print(result)
# print("boxes:")
# for box in result[0].boxes:
#     print(box)

