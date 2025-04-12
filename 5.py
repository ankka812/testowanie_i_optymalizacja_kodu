import cv2
import numpy as np

image = cv2.imread('fox.jpg')
cv2.imshow("Original", image)

rows, cols = image.shape[:2]
M = np.float32([[1, 0, 20], [0, 1, 0]])
changed = cv2.warpAffine(image, M, (cols, rows))

diff = cv2.absdiff(image, changed)

cv2.imshow("Original", image)
cv2.imshow("Changed", changed)
cv2.imshow("Difference", diff)
cv2.waitKey(0)
