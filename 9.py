import cv2
#800x798
image = cv2.imread('obraz.jpg')

(h,w)=image.shape[:2]

startX = (w - 300) // 2
startY = (h - 300) // 2

cropped = image[startY:startY+300, startX:startX+300]

cv2.imshow('cropped', cropped)
cv2.waitKey(0)

cv2.imwrite('cropped_image.jpg', cropped)
