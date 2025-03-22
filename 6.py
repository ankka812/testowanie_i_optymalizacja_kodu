import argparse
import imutils
import cv2

image = cv2.imread("pieski.jpg")
cv2.imshow("Original", image)

rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated Without Cropping", rotated)
cv2.waitKey(0)

