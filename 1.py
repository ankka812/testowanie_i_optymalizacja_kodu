import cv2

image = cv2.imread("piesek.jpg")

kernel_sizes = [3, 9, 15]

for k in kernel_sizes:
    blurred_avg = cv2.blur(image, (k, k))
    blurred_gaussian = cv2.GaussianBlur(image, (k, k), 0)
    blurred_median = cv2.medianBlur(image, k)
    blurred_bilateral = cv2.bilateralFilter(image, k, 75, 75)

    cv2.imshow(f"Original", image)
    cv2.imshow(f"Average Blur {k}x{k}", blurred_avg)
    cv2.imshow(f"Gaussian Blur {k}x{k}", blurred_gaussian)
    cv2.imshow(f"Median Blur {k}", blurred_median)
    cv2.imshow(f"Bilateral Filter {k}", blurred_bilateral)
    cv2.waitKey(0)

cv2.destroyAllWindows()


#i. Która metoda najlepiej usuwa szum?
#medianBlur
#ii. Która metoda zachowuje najwięcej szczegółów?
#bilateralFilter
#iii. Jakie są zalety i wady każdej metody?
#blur: szybkie, ale traci detale
#GaussianBlur: lepsze niz blur, ale rozmywa krawedzie
#medianBlur: dobre na szum, ale gubi fakture
#bilateralFilter: zachowuje krawedzie, ale wolne





