import cv2

image = cv2.imread('shapes.png', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

shapes = {
    "Rect": cv2.MORPH_RECT,
    "Ellipse": cv2.MORPH_ELLIPSE,
    "Cross": cv2.MORPH_CROSS
}

morphs = {
    "Erode": cv2.MORPH_ERODE,
    "Dilate": cv2.MORPH_DILATE,
    "Open": cv2.MORPH_OPEN,
    "Close": cv2.MORPH_CLOSE,
    "Gradient": cv2.MORPH_GRADIENT
}

for shape_name, shape in shapes.items():
    kernel = cv2.getStructuringElement(shape, (5, 5))
    for op_name, op in morphs.items():
        result = cv2.morphologyEx(binary, op, kernel)
        cv2.imshow(f"{op_name} - {shape_name}", result)
        cv2.waitKey(0)

cv2.destroyAllWindows()