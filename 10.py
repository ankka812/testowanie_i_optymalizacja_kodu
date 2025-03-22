import argparse
import imutils
import cv2

image = cv2.imread("pieski.jpg")
cv2.imshow("Original", image)

for s in range(0,360,15):
    rotated = imutils.rotate_bound(image,s)
    cv2.imshow("Rotated Without Cropping", rotated)
    cv2.waitKey(500)