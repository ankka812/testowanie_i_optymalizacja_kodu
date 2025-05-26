import cv2
import numpy as np

image = cv2.imread("photo.jpg")

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (0, 100), (200, 300), 255, -1)

blurred = cv2.GaussianBlur(image, (25, 25), 0)

focused = np.where(mask[:, :, None] == 255, image, blurred)

cv2.imshow("Original", image)
cv2.imshow("Simulated DoF", focused)
cv2.waitKey(0)
cv2.destroyAllWindows()



