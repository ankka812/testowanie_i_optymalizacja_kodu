import argparse
import imutils
import cv2

image = cv2.imread("pieski.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]

M = cv2.getRotationMatrix2D((10, 10), 30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by Arbitrary Point", rotated)
cv2.waitKey(0)