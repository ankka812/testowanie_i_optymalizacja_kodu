import cv2

image = cv2.imread("piesek.jpg")

kernel_sizes = [3, 5, 9, 15]

for k in kernel_sizes:
    avg = cv2.blur(image, (k, k))
    cv2.imshow(f"Average Blur {k}x{k}", avg)

    gauss = cv2.GaussianBlur(image, (k, k), 0)
    cv2.imshow(f"Gaussian Blur {k}x{k}", gauss)

    med = cv2.medianBlur(image, k)
    cv2.imshow(f"Median Blur {k}", med)

    bilateral = cv2.bilateralFilter(image, k, 75, 75)
    cv2.imshow(f"Bilateral Filter {k}", bilateral)

    cv2.waitKey(1000)

cv2.destroyAllWindows()

#i. Jak zmienia się efekt rozmycia w zależności od wielkości kernela?
#im wiekszy kernel, tym mocniejsze rozmycie i mniej detali
#ii. Jaki rozmiar kernela jest optymalny dla redukcji szumu bez utraty istotnych detali?
#5 lub 9 - balans miedzy redukcja szumu a zachowaniem szczegolow

