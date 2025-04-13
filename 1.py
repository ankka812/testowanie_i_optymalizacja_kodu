import cv2
import numpy as np

image = cv2.imread("person.jpg")
cv2.imshow("Original", image)


mask = np.zeros(image.shape[:2], dtype="uint8")
center_x = image.shape[1] // 2 + 10
center_y = image.shape[0] // 2 - 30
cv2.ellipse(mask, (center_x, center_y), (40, 50), 0, 0, 360, 255, -1)

masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Masked Face", masked)
cv2.waitKey(0)