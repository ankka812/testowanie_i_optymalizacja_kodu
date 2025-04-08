
import cv2
#800x798
image = cv2.imread('obraz.jpg')
cv2.imshow('image', image)

(h,w)=image.shape[:2]

h_step = h // 3
w_step = w // 3

for i in range(3):
    for j in range(3):
        roi = image[i*h_step:(i+1)*h_step, j*w_step:(j+1)*w_step]

        cv2.imshow(f"Part {i*3 + j + 1}", roi)

cv2.waitKey(0)