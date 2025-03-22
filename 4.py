import argparse
import imutils
import cv2

s = int(input("O ile stopni obrocic obraz? "))

image = cv2.imread("pieski.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), s, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("After changes", rotated)
cv2.waitKey(0)