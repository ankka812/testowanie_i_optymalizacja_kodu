import cv2
image = cv2.imread('piesek.jpg')
(h, w) = image.shape[:2]

(cX, cY) = (w // 2, h // 2)

square_size = 100
half_size = square_size // 2

x1, y1 = cX - half_size, cY - half_size
x2, y2 = cX + half_size, cY + half_size

top_left_x = cX - half_size
top_left_y = cY - half_size

image[top_left_y:top_left_y + square_size, top_left_x:top_left_x + square_size] = [0, 0, 255]

cv2.imshow("Obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
