import cv2

option = int(input("odwrocenie zdjecia pionowe(1), poziome(2), oba(-1): "))

image = cv2.imread("puma.jpg")
cv2.imshow("Original", image)

if option == -1:
    flipped = cv2.flip(image, -1)
    cv2.imshow("Flipped Horizontally & Vertically", flipped)

elif option == 0:
    flipped = cv2.flip(image, 0)
    cv2.imshow("Flipped Vertically", flipped)

elif option == 1:
    flipped = cv2.flip(image, 1)
    cv2.imshow("Flipped Horizontally", flipped)

cv2.waitKey(0)




