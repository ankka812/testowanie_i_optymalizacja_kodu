import cv2

image = cv2.imread('tiger.jpg', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
kernels = [(3, 3), (5, 5), (7, 7)]

for size in kernels:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    cv2.imshow(f"Opening {size}", opening)
    cv2.waitKey(0)

cv2.destroyAllWindows()












