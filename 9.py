import argparse
import imutils
import cv2

image = cv2.imread("pieski.jpg")
cv2.imshow("Original", image)

rotated = imutils.rotate_bound(image, 75)
cv2.imwrite("rotated_output.jpg", rotated)
cv2.waitKey(0)