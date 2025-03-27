import cv2
import imutils

image = cv2.imread("antylopa.jpg")
cv2.imshow("Original", image)

resized = imutils.resize(image, width=image.shape[1] * 2, height=image.shape[0] * 2, inter=cv2.INTER_LINEAR)
cv2.imshow("Resized 2x", resized)

cv2.waitKey(0)




