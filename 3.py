import cv2
import numpy as np
image = cv2.imread('fox.jpg')
cv2.imshow("Original", image)

numpy = image - 80
cv2.imshow("cv2", numpy)

M = np.ones(image.shape, dtype="uint8") * 80
opencv = cv2.subtract(image, M)
cv2.imshow("np", opencv)
cv2.waitKey(0)