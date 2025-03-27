import cv2

image = cv2.imread("antylopa.jpg")
cv2.imshow("Original", image)

new_size = (image.shape[1] * 4, image.shape[0] * 4)

resized_cubic = cv2.resize(image, new_size, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Resized INTER_CUBIC", resized_cubic)

resized_lanczos = cv2.resize(image, new_size, interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("Resized INTER_LANCZOS4", resized_lanczos)

cv2.waitKey(0)


