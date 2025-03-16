import cv2
image = cv2.imread('piesek.jpg')
(h, w) = image.shape[:2]

cv2.imshow("przed zmiana", image)

image[h-1, w-1] = (0, 0, 255)

cv2.imshow("po zmianie", image) # Tworzy okno i wyświetla obraz
cv2.waitKey(0) # Czeka na dowolny klawisz, by zamknąć okno
cv2.destroyAllWindows() # Zamknięcie wszystkich okien
