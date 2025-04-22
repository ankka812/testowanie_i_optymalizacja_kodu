import cv2

image = cv2.imread('black.png', cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

eroded_square = cv2.erode(binary, kernel_square, iterations=1)
eroded_ellipse = cv2.erode(binary, kernel_ellipse, iterations=1)

cv2.imshow("Original", binary)
cv2.imshow("Erosion - Square", eroded_square)
cv2.imshow("Erosion - Elliptical", eroded_ellipse)
cv2.waitKey(0)
cv2.destroyAllWindows()