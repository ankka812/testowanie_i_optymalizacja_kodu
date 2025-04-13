import cv2
import numpy as np

image = cv2.imread("car.jpg")

(B, G, R) = cv2.split(image)
mask = cv2.inRange(R, 150, 255)

R_boosted = cv2.add(R, 100)
R_boosted = np.where(mask == 255, R_boosted, R)
R_boosted = np.clip(R_boosted, 0, 255).astype("uint8")

modified = cv2.merge([B, G, R_boosted])

cv2.imshow("Original", image)
cv2.imshow("Modified Red Channel", modified)
cv2.waitKey(0)


