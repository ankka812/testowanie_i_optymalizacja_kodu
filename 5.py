
import cv2
#280x180
image = cv2.imread('twarz.jpg')
cv2.imshow('image', image)

roi = image[0:125, 90:190]

cv2.imshow('roi', roi)

cv2.waitKey(0)