import cv2
image = cv2.imread('piesek.jpg')
(h, w) = image.shape[:2]

max_brightness = -1
max_pixel = None
coordinates = None

for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        R, G, B = image[y, x]
        brightness = 0.299 * R + 0.587 * G + 0.114 * B

        if brightness > max_brightness:
            max_brightness = brightness
            max_pixel = (R, G, B)
            coordinates = (y, x)

print(f"Najjaśniejszy piksel znajduje się na współrzędnych: {coordinates}")
print(f"Jego wartość RGB to: {max_pixel}")
