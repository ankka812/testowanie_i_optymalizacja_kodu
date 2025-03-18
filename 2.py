import cv2
import numpy as np

canvas = np.zeros((400, 400, 3), dtype="uint8")
cv2.rectangle(canvas, (0,0), (100, 50), (0,128,0))
cv2.rectangle(canvas, (300, 350), (399, 399), (0, 0, 255), 3)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)