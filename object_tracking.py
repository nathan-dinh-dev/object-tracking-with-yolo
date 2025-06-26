import cv2
import numpy as np
import torch
from deep_sort_realtime.deepsort_tracker import DeepSort
from yolov9.models.common import DetectMultiBackend, AutoShape

# Config for YOLOv9 model
video_path = "data/highway.mp4"

# If it's over 0.5, it will be considered a valid detection
confidence_threshold = 0.5

tracking_class = 2  # 2 is for car in COCO dataset

# Initialize DeepSort
# Maximum age of 5 frames. If an object is not detected for 5 consecutive frames, its tracker is removed (i.e., considered gone).
tracker = DeepSort(max_age=5)

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load YOLOv9 model
model = DetectMultiBackend(weights="weights/yolov9-c.pt", device=device, fuse=True)
model = AutoShape(model)

# Load classname from classes.names
with open("data_ext/classes.names", "r") as f:
    class_names = f.read().strip().splitlines()


colors = np.random.randint(0, 255, size=(len(class_names), 3))

# This to store the tracks
tracks = []

# Initialize video capture
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Bring it to model
    results = model(frame)

    detect = []

    for detect_object in results.pred[0]:
        label, confidence, bbox = detect_object[5], detect_object[4], detect_object[:4]
        x1, y1, x2, y2 = map(int, bbox)
        class_id = int(label)

        if tracking_class is None:
            if confidence < confidence_threshold:
                continue
        else:
            if class_id != tracking_class or confidence < confidence_threshold:
                continue

        detect.append([[x1, y1, x2, y2], confidence, class_id])

    # Update the tracker with the detections
    tracks = tracker.update_tracks(detect, frame=frame)

    # Draw the tracks on the frame
    for track in tracks:
        if track.is_confirmed():
            track_id = track.track_id

            # Get the bounding box and class ID
            bbox = track.to_tlbr()
            class_id = track.get_det_class()
            x1, y1, x2, y2 = map(int, bbox)
            color = colors[class_id]
            B, G, R = map(int, color)

            label = "{}-{}".format(class_names[class_id], track_id)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (B, G, R), 2)
            cv2.rectangle(
                frame, (x1 - 1, y1 - 20), (x1 + len(label) * 12, y1), (B, G, R), -1
            )
            cv2.putText(
                frame,
                label,
                (x1 + 5, y1 - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                2,
            )

    # Show hình ảnh lên màn hình
    cv2.imshow("OT", frame)
    # Bấm Q thì thoát
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
