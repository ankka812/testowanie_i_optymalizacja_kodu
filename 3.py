import cv2
image = cv2.imread('piesek.jpg')
(h, w) = image.shape[:2]

cv2.imshow("przed zmiana", image)
cv2.waitKey(0) # Czeka na dowolny klawisz, by zamknąć okno
cv2.destroyAllWindows() # Zamknięcie wszystkich okien

(cX, cY) = (w // 2, h // 2)

print(f"Środek: ({cX}, {cY}), Kolor (BGR): {image[cY, cX]}")