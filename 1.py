import cv2

image = cv2.imread("antylopa.jpg")
cv2.imshow("Original", image)

resized = cv2.resize(image, (112, 112), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", resized)

cv2.waitKey(0)

