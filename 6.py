import cv2
import imutils

image = cv2.imread("antylopa.jpg")
cv2.imshow("Original", image)

resized = imutils.resize(image, height=400)
cv2.imshow("Resized to 400px height", resized)

cv2.waitKey(0)