import cv2

image = cv2.imread("puma.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]

half = image[:, w // 2 :]

flipped_half = cv2.flip(half, 1)

image[:, w // 2 :] = flipped_half

cv2.imshow("Image", image)
cv2.waitKey(0)

