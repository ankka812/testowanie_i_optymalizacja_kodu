import cv2

image = cv2.imread("text.png")

kernel_size = 9

blur_avg = cv2.blur(image, (kernel_size, kernel_size))
cv2.imshow("Average Blur", blur_avg)

blur_gaussian = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
cv2.imshow("Gaussian Blur", blur_gaussian)

blur_median = cv2.medianBlur(image, kernel_size)
cv2.imshow("Median Blur", blur_median)

blur_bilateral = cv2.bilateralFilter(image, kernel_size, 100, 100)
cv2.imshow("Bilateral Filter", blur_bilateral)

cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#i. Które metody najmocniej rozmywają tekst?
#Avarage i Gaussian
#ii. Które pozwalają zachować jego czytelność?
#Median i Bilateral