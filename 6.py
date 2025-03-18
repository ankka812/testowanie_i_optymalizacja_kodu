import cv2
import numpy as np

image = cv2.imread("twarz.jpg")

cv2.circle(image, (75,100), 7, (0, 0, 255))
cv2.circle(image, (115,100), 7, (0, 0, 255))

cv2.rectangle(image, (80, 150), (110, 130), (0, 255, 0))

cv2.circle(image, (95,105), 60, (255, 0, 0))

cv2.imshow("Canvas", image)
cv2.waitKey(0)
