import cv2
import numpy as np
import time
import HandTrackingModule as htm

############################
brushThickness = 15
eraserThickness = 60
############################

cap = cv2.VideoCapture(0)

# Lower resolution = smoother performance
cap.set(3, 960)
cap.set(4, 540)

detector = htm.handDetector(detectionCon=0.7, maxHands=1)

success, img = cap.read()

# Automatically match canvas size to camera
h, w, _ = img.shape
imgCanvas = np.zeros((h, w, 3), np.uint8)

xp, yp = 0, 0

drawColor = (255, 0, 255)

pTime = 0

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)

    if len(lmList) != 0:

        x1, y1 = lmList[8][1:]   # index finger
        x2, y2 = lmList[12][1:]  # middle finger

        fingers = detector.fingersUp()

        # -------- COLOR PALETTE --------
        paletteHeight = 60

        colors = [
            (255,0,255),  # pink
            (255,0,0),    # blue
            (0,255,0),    # green
            (0,0,0)       # eraser
        ]

        sectionWidth = w // len(colors)

        for i, color in enumerate(colors):
            cv2.rectangle(img,
                          (i*sectionWidth,0),
                          ((i+1)*sectionWidth,paletteHeight),
                          color,
                          cv2.FILLED)

        # -------- SELECTION MODE --------
        if fingers[1] and fingers[2]:

            xp, yp = 0, 0

            if y1 < paletteHeight:

                index = x1 // sectionWidth
                if index < len(colors):
                    drawColor = colors[index]

            cv2.rectangle(img,
                          (x1, y1-25),
                          (x2, y2+25),
                          drawColor,
                          cv2.FILLED)

        # -------- DRAW MODE --------
        elif fingers[1] and not fingers[2]:

            cv2.circle(img,(x1,y1),10,drawColor,cv2.FILLED)

            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            thickness = eraserThickness if drawColor == (0,0,0) else brushThickness

            cv2.line(imgCanvas,(xp,yp),(x1,y1),drawColor,thickness)

            xp, yp = x1, y1

        else:
            xp, yp = 0, 0

    # -------- MERGE CANVAS --------

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)

    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)

    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    # -------- FPS COUNTER --------

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, h-20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    cv2.imshow("Virtual Painter", img)

    cv2.waitKey(1)