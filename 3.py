
import cv2
#800x798
image = cv2.imread('obraz.jpg')
cv2.imshow('image', image)

roi = image[0:800, 399:798]

cv2.imshow('roi', roi)

cv2.waitKey(0)