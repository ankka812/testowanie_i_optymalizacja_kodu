import cv2
image_gray = cv2.imread("kotek.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Obraz w skali szarości", image_gray)

(h, w) = image_gray.shape[:3]
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: 1')

cv2.waitKey(0)
cv2.destroyAllWindows()