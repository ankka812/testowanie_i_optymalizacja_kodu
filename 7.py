import cv2
image = cv2.imread('piesek.jpg')
(h, w) = image.shape[:2]

(cX, cY) = (w // 3, h // 3)

centerX = cX
centerX2 = 2 * cX
centerY = cY
centerY2 = 2 * cY

center_fragment = image[centerY:centerY2, centerX:centerX2]

cv2.imshow("Obraz", center_fragment)
cv2.waitKey(0)
cv2.destroyAllWindows()