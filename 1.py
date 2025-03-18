import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
black = (255, 0, 0)
x2, y2 = canvas.shape[1] - 1, canvas.shape[0] - 1

cv2.line(canvas, (centerX, centerY), (x2, y2), black, 2)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
