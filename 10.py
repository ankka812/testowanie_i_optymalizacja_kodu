import cv2
image = cv2.imread('piesek.jpg')
(h, w) = image.shape[:2]

pixel1 = image[50,50]
pixel2 = image[200,200]

differenceR = pixel1[0] - pixel2[0]
differenceG = pixel1[1] - pixel2[1]
differenceB = pixel1[2] - pixel2[2]

print(f"Różnica w wartości R: {differenceR}")
print(f"Różnica w wartości G: {differenceG}")
print(f"Różnica w wartości B: {differenceB}")