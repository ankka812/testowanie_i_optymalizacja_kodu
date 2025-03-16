import cv2
image = cv2.imread('piesek.jpg')
(h, w) = image.shape[:2]

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

cv2.imshow("Wyświetlony obraz", image) # Tworzy okno i wyświetla obraz
cv2.waitKey(0) # Czeka na dowolny klawisz, by zamknąć okno
cv2.destroyAllWindows() # Zamknięcie wszystkich okien

