import cv2
import imutils

image = cv2.imread("antylopa.jpg")
cv2.imshow("Original", image)

resized = imutils.resize(image, width=500)
cv2.imshow("Resized to 500px width", resized)

cv2.waitKey(0)


