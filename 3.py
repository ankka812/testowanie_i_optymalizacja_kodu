import cv2
import numpy as np

canvas = np.zeros((400, 400, 3), dtype="uint8")
cv2.circle(canvas, (40, 40), 40, (255, 0, 0))
cv2.circle(canvas, (200, 200), 60, (0, 0, 255))

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)