from ultralytics import YOLO
import cv2

# YOLOv8 model (you can choose 'yolov8n', 'yolov8s', 'yolov8m', 'yolov8l', 'yolov8x')
model = YOLO('yolov8m.pt')  # 'yolov8l.pt' is the large model; you can choose smaller versions for speed

def detect_and_count_vehicles(video_source):
    cap = cv2.VideoCapture(video_source)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Perform inference on the frame
        results = model(frame)

        vehicle_count = 0

        #TEST CODE FOR SEPERATE VEHICLE COUNTING
        car_count = 0
        bus_count=0
        motorcycle_count=0
        truck_count=0


        # Iterate over each detection result
        for result in results:
            boxes = result.boxes
            for box in boxes:
                # Extract bounding box coordinates
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()  # Extract coordinates
                conf = box.conf[0].item()  # Extract confidence score
                cls = int(box.cls[0].item())  # Extract class ID

                # Check for vehicle classes: 2-car, 3-motorcycle, 5-bus, 7-truck
                if cls in [2, 3, 5, 7]:
                    vehicle_count += 1
                    label = f"{model.names[cls]} {conf:.2f}"
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                #TEST CODE FOR COUNTING SEPERATE VEHICLES
                if cls in[2]:
                    car_count+=1;
                if cls in [3]:
                    motorcycle_count+=1;
                if cls in [5]:
                    bus_count+=1;
                if cls in [7]:
                    truck_count+=1;

        # Display the vehicle count on the frame
        #cv2.putText(frame, f'Vehicles Counted: {vehicle_count}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Display the total vehicle count
        cv2.putText(frame, f'Vehicles Counted: {vehicle_count}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Display each vehicle type count on new lines by incrementing the Y-coordinate
        cv2.putText(frame, f'Car Count: {car_count}', (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame, f'Motorcycle Count: {motorcycle_count}', (20, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame, f'Bus Count: {bus_count}', (20, 160), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame, f'Truck Count: {truck_count}', (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Show the processed frame
        cv2.imshow('Vehicle Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage with a video file or live camera feed (use 0 for webcam)
#video_path = "C:/Users/VEDANT/Downloads/Untitled video - Made with Clipchamp.mp4"

video_path = "C:/Users/VEDANT/Desktop/istockphoto-1372690761-640_adpp_is.mp4"
detect_and_count_vehicles(video_path)  # Replace with '0' for webcam
