import cv2

image = cv2.imread("zima.jpg")

params = [
    (9, 50, 50),
    (9, 100, 100),
    (9, 150, 150)
]

for (d, sc, ss) in params:
    bilateral = cv2.bilateralFilter(image, d, sc, ss)
    cv2.imshow(f"Bilateral d={d}, sc={sc}, ss={ss}", bilateral)
    cv2.waitKey(1000)

cv2.imshow("Original", image)
cv2.imshow("Average Blur", cv2.blur(image, (9, 9)))
cv2.imshow("Gaussian Blur", cv2.GaussianBlur(image, (9, 9), 0))
cv2.imshow("Median Blur", cv2.medianBlur(image, 9))
cv2.waitKey(0)
cv2.destroyAllWindows()

#i. Czy rozmycie dwustronne skutecznie redukuje szum?
#tak
#ii. Czy zachowuje lepiej krawędzie w porównaniu do innych metod?
#tak
#iii. Jakie wartości parametrów dają najlepsze rezultaty?
#najlepszy balans to (9,100,100)