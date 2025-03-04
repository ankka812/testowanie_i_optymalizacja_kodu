import cv2
# Wczytanie obrazu z pliku
image = cv2.imread("kotek.jpg")
# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

cv2.imshow("Wyświetlony obraz", image) # Tworzy okno i wyświetla obraz
cv2.waitKey(0) # Czeka na dowolny klawisz, by zamknąć okno
cv2.destroyAllWindows() # Zamknięcie wszystkich okien