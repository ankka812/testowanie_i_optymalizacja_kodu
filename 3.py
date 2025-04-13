import cv2
import numpy as np
image = cv2.imread("flowers.jpg")
(B, G, R) = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

merged = cv2.merge([R, G, B])
cv2.imshow("Merged", merged)

zero = cv2.merge([R, G, np.zeros_like(R)])
cv2.imshow("zero", zero)

cv2.waitKey(0)



