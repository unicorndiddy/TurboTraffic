import json
import cv2
from ultralytics import YOLO

model = YOLO('yolov8m.pt')

def detect_and_count_vehicles(video_source):
    cap = cv2.VideoCapture(video_source)
    output_data = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        vehicle_count = 0
        car_count = 0
        bus_count = 0
        motorcycle_count = 0
        truck_count = 0

        for result in results:
            boxes = result.boxes
            for box in boxes:
                cls = int(box.cls[0].item())
                if cls in [2, 3, 5, 7]:
                    vehicle_count += 1
                    if cls == 2: car_count += 1
                    if cls == 3: motorcycle_count += 1
                    if cls == 5: bus_count += 1
                    if cls == 7: truck_count += 1

        frame_data = {
            "vehicle_count": vehicle_count,
            "car_count": car_count,
            "motorcycle_count": motorcycle_count,
            "bus_count": bus_count,
            "truck_count": truck_count
        }

        output_data.append(frame_data)

    cap.release()
    return output_data

if __name__ == "__main__":
    import sys
    video_path = sys.argv[1]
    data = detect_and_count_vehicles(video_path)
    print(json.dumps(data))
