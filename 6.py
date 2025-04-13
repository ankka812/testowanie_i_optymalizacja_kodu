import cv2
import numpy as np

image = cv2.imread("flowers.jpg")
(B, G, R) = cv2.split(image)

cv2.imshow("Blue Channel", B)
cv2.imshow("Green Channel", G)
cv2.imshow("Red Channel", R)

swapped = cv2.merge([R, G, B])
cv2.imshow("swapped", swapped)

zero_channel = np.zeros_like(B)
removed_G = cv2.merge([B, zero_channel, R])

cv2.imshow("Without Green Channel", removed_G)
cv2.waitKey(0)











