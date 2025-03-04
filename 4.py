import cv2

image_gray = cv2.imread("kotek.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("new_gray_photo.jpg", image_gray)

