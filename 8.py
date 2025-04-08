
import cv2
#800x798
image = cv2.imread('obraz.jpg')

(h,w)=image.shape[:2]

r_width = 400
r_height = 400
step = 10
startX = 0
startY = max(0, (h - r_height) // 2)

while True:
    startX = min(max(0, startX), w - r_width)
    roi = image[startY:startY+r_height, startX:startX+r_width]

    cv2.imshow('roi', roi)
    key = cv2.waitKey(0)
    if key == 27:
        break
    startX = startX + step
    if startX + r_width > w:
        startX = 0

