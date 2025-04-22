import cv2

image = cv2.imread('black.png', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

shapes = {
    "Rect": cv2.MORPH_RECT,
    "Ellipse": cv2.MORPH_ELLIPSE,
    "Cross": cv2.MORPH_CROSS
}

for name, shape in shapes.items():
    kernel = cv2.getStructuringElement(shape, (5, 5))
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    cv2.imshow(f"Closing - {name}", closing)
    cv2.waitKey(0)

cv2.destroyAllWindows()