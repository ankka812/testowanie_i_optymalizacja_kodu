import cv2
import numpy as np

canvas = np.zeros((400, 400, 3), dtype="uint8")
centerX, centerY = canvas.shape[1] // 2, canvas.shape[0] // 2
for r in range(20, 400, 20):
    half = r // 2
    x1, y1 = centerX - half, centerY - half
    x2, y2 = centerX + half, centerY + half
    cv2.rectangle(canvas, (x1, y1), (x2, y2), (255, 255, 255))

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)