import numpy as np
import cv2

tx = int(input("O ile przesunac obraz w lewo lub w prawo? "))
ty = int(input("O ile przesunac obraz w gore lub w dol? "))

image = cv2.imread("piesek.jpg")    #275x183
cv2.imshow("Original", image)

M = np.float32([[1, 0, tx], [0, 1, ty]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("After changes", shifted)
cv2.waitKey(0)

