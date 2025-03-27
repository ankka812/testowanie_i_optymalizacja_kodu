import cv2

image = cv2.imread("puma.jpg")
cv2.imshow("Original", image)

flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

flipped2 = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped2)

flipped3 = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped3)

cv2.waitKey(0)