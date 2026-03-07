# Hand Tracking Painter — Gesture-Controlled Drawing Application

A real-time computer vision application built with Python, OpenCV, and MediaPipe that allows users to draw on a virtual canvas using hand gestures captured from a webcam.

Hand Tracking Painter transforms hand movements into digital brush strokes by tracking finger landmarks and interpreting gestures for drawing, erasing, and color selection. The project demonstrates real-time hand tracking, gesture recognition, and interactive visual interfaces using modern computer vision tools.

## ✨ Introduction

Hand Tracking Painter is designed as an interactive computer vision application where users can control a digital canvas entirely through hand gestures.

Using MediaPipe's hand landmark detection system, the program tracks finger positions in real time and converts them into drawing actions. Different gestures allow users to switch between drawing mode, selection mode, and erasing, enabling a hands-free painting experience.

This project highlights the capabilities of gesture recognition and real-time image processing, making it a strong demonstration of practical computer vision applications.

## 📌 Project Overview

This application allows users to:

* Draw on a virtual canvas using finger movements  
* Switch between drawing and selection modes using gestures  
* Select different brush colors from a gesture-controlled palette  
* Erase drawings using an eraser gesture  
* Interact with the canvas in real time using a webcam  

## 🔋 Features

**Real-Time Hand Tracking** — Uses MediaPipe to detect and track 21 hand landmarks with high accuracy

**Gesture-Based Drawing** — Draw on a virtual canvas using the index finger as a digital brush

**Selection Mode** — Raise two fingers to switch from drawing to tool selection

**Color Palette** — Choose different brush colors through gesture interaction

**Eraser Tool** — Remove parts of the drawing using a gesture-based eraser

**Smooth Drawing Optimization** — Improved drawing stability with motion smoothing and reduced lag

**Virtual Canvas Rendering** — Combines webcam frames with a transparent drawing layer for a seamless experience

## 🧠 How It Works

The system uses MediaPipe's hand tracking model to detect **21 hand landmarks** in real time.

1. The webcam captures frames continuously.
2. MediaPipe identifies the hand and extracts landmark positions.
3. The program monitors the position of the **index finger tip** and **middle finger tip**.
4. Gestures determine the current interaction mode.

Gesture logic:

| Gesture | Action |
|-------|-------|
| Index finger up | Drawing mode |
| Index + middle finger up | Selection mode |
| Eraser selected | Erase drawing |

Finger movements are mapped to screen coordinates and rendered on a virtual canvas layered over the webcam feed.

## 🛠 Tech Stack

Python  
OpenCV  
MediaPipe  
NumPy  

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/batoolag/hand-tracking-painter.git
cd hand-tracking-painter
```

### 2. Install dependencies

```bash
pip install opencv-python mediapipe numpy
```

### 3. Run the application

```bash
python VirtualPainter.py
```
