import cv2
import numpy as np

image = cv2.imread("piesek.jpg")

noisy = image.copy()
noise = np.zeros_like(image, dtype=np.int16)
cv2.randn(noise, (0, 0, 0), (30, 30, 30))
noisy = cv2.add(image.astype(np.int16), noise)
noisy = np.clip(noisy, 0, 255).astype(np.uint8)

cv2.imshow("Noisy Image (Gaussian)", noisy)

kernel = 5

avg = cv2.blur(noisy, (kernel, kernel))
gaussian = cv2.GaussianBlur(noisy, (kernel, kernel), 0)
median = cv2.medianBlur(noisy, kernel)
bilateral = cv2.bilateralFilter(noisy, kernel, 75, 75)

cv2.imshow("Average Blur", avg)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Blur", median)
cv2.imshow("Bilateral Filter", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

