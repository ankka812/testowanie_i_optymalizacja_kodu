import cv2
image = cv2.imread('piesek.jpg')
(h, w) = image.shape[:2]

cv2.imshow("przed zmiana", image)

image[99, :, :] = [0, 255, 0]

cv2.imshow("po zmianie", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
