
import cv2
#800x798
image = cv2.imread('obraz.jpg')
cv2.imshow('image', image)

roi = image[0:100, 0:100]

(h,w)=image.shape[:2]
roi = image[h-100:h, w-100:w]

cv2.imshow('roi', roi)

cv2.waitKey(0)