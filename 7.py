import argparse
import imutils
import cv2

image = cv2.imread("pieski.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("cv2.warpAffine", rotated)

rotated = imutils.rotate(image, 60)
cv2.imshow("imutils.rotate", rotated)
cv2.waitKey(0)
# obrazki wygladaja tak samo