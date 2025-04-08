
import cv2

startX = int(input("podaj startX: "))
endX = int(input("podaj endX: "))
startY = int(input("podaj startY: "))
endY = int(input("podaj endY: "))

#800x798
image = cv2.imread('obraz.jpg')
cv2.imshow('image', image)

roi = image[startX:endX, startY:endY]

cv2.imshow('roi', roi)

cv2.waitKey(0)