import cv2
import imutils

image = cv2.imread("piesek.jpg")    #275x183
cv2.imshow("Original", image)

shifted = imutils.translate(image, 100, 50)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)