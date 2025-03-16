import cv2
image = cv2.imread('piesek.jpg')
(h, w) = image.shape[:2]

(cX, cY) = (w // 2, h // 2)

image[:cY, :cX] = (255, 0, 0)

cv2.imshow("Obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()