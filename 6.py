import cv2

image = cv2.imread("kotek.jpg")

cv2.namedWindow("kotek", cv2.WINDOW_NORMAL)
cv2.imshow("kotek", image)

cv2.waitKey(0)
cv2.destroyAllWindows()