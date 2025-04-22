import cv2

image = cv2.imread('tablica.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

morphed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original", image)
cv2.imshow("Morphed Plate", morphed)
cv2.waitKey(0)
cv2.destroyAllWindows()

