import cv2

image1 = cv2.imread("kotek.jpg")
image2 = cv2.imread("kotek2.jpg")

cv2.imshow("kotek 1", image1)
cv2.imshow("kotek2 2", image2)

cv2.waitKey(0)
cv2.destroyAllWindows()