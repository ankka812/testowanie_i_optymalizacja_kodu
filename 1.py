import cv2
import numpy as np
image = cv2.imread('fox.jpg')
cv2.imshow("Original", image)

added = image + 50
cv2.imshow("cv2", added)

M = np.ones(image.shape, dtype="uint8") * 50
added2 = cv2.add(image, M)
cv2.imshow("np", added2)
cv2.waitKey(0)


