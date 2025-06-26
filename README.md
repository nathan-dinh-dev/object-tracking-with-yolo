# DeepSORT_Yolov9

🚗🎯 Real-time object tracking using **YOLOv9** and **DeepSORT**.

This project demonstrates how to combine YOLOv9 for object detection and DeepSORT for multi-object tracking across video frames.

---

## 🔗 YOLOv9 Repository

To get the YOLOv9 model code and weights, clone from the official repo:

> 🔗 [YOLOv9 GitHub – WongKinYiu](https://github.com/WongKinYiu/yolov9)

Place the `yolov9/` directory from that repo into your project folder.

---

## 📁 Features

- Object detection with **YOLOv9**
- Identity-preserving tracking with **DeepSORT**
- Real-time tracking on video input
- Class-specific filtering (e.g., only track cars)
- OpenCV visualization with bounding boxes and track IDs

---

## 🛠 Requirements

- Python 3.8+
- PyTorch
- OpenCV
- NumPy
- [`deep_sort_realtime`](https://pypi.org/project/deep-sort-realtime/)
- YOLOv9 code from the repo above

---

## 🚀 Getting Started

1. **Clone this project**:

   ```bash
   git clone https://github.com/yourusername/DeepSORT_Yolov9.git
   cd DeepSORT_Yolov9
   ```

2. **Download and place YOLOv9**:

   - Clone the [YOLOv9 GitHub repo](https://github.com/WongKinYiu/yolov9)
   - Copy the `yolov9/` folder into this project directory

3. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Download YOLOv9 weights** (e.g., `yolov9-c.pt`) and place them in the `weights/` folder.

5. **Add class names**:

   - Create `data_ext/classes.names` with COCO class names or your custom classes.

6. **Run the tracker**:
   ```bash
   python object_tracking.py
   ```

---

## 📂 Project Structure

```
DeepSORT_Yolov9/
├── object_tracking.py         # Main tracking script
├── yolov9/                    # YOLOv9 model code (from GitHub)
├── weights/
│   └── yolov9-c.pt            # YOLOv9 model weights
├── data/
│   └── highway.mp4            # Input video
├── data_ext/
│   └── classes.names          # List of class labels
└── README.md
```

---

## 📸 Output

- Real-time video window with:
  - Bounding boxes
  - Class name + unique tracking ID
- Press `Q` to exit the window

---

## 📜 License

This is an open-source project for learning and demonstration purposes. Original YOLOv9 is licensed under the terms of the [YOLOv9 repository](https://github.com/WongKinYiu/yolov9).
