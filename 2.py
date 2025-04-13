import cv2
import numpy as np

image = cv2.imread("person.jpg")
cv2.imshow("Original", image)

mask = np.ones(image.shape, dtype="uint8") * 255

cv2.rectangle(mask, (100, 60), (150, 80), (0, 0, 0), -1)

masked = cv2.bitwise_and(image, mask)

cv2.imshow("Eyes Hidden", masked)
cv2.waitKey(0)




