import cv2

image = cv2.imread("antylopa.jpg")
cv2.imshow("Original", image)

for i in range(100, 301, 20):
    f = i / 100
    new_size = (int(image.shape[1] * f), int(image.shape[0] * f))

    resized = cv2.resize(image, new_size, interpolation=cv2.INTER_LINEAR)

    cv2.imshow(f"scaled {i}%", resized)
    cv2.waitKey(500)
