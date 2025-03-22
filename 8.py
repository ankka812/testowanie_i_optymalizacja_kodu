import argparse
import imutils
import cv2

image = cv2.imread("pieski.jpg")
cv2.imshow("Original", image)

rotated = imutils.rotate_bound(image, 30)
rotated2 = imutils.rotate_bound(rotated, 30)
rotated3 = imutils.rotate_bound(rotated2, 30)

rotated4 = imutils.rotate_bound(image, 90)

cv2.imshow("1", rotated3)
cv2.imshow("2", rotated4)
cv2.waitKey(0)