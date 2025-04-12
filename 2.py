import cv2

image1 = cv2.imread("fox.jpg")
image2 = cv2.imread("fox.jpg")

image2 = image2[10:, :]

image1 = image1[:image2.shape[0], :image2.shape[1]]

difference = cv2.bitwise_xor(image1, image2)

cv2.imshow("Image 1", image1)
cv2.imshow("Image 2", image2)
cv2.imshow("Difference (XOR)", difference)

cv2.waitKey(0)
