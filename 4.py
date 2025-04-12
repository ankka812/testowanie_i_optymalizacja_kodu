import cv2

image = cv2.imread('fox.jpg')
cv2.imshow("Original", image)

(B, G, R) = cv2.split(image)

R = cv2.add(R, 30)
G = cv2.subtract(G, 20)
B = cv2.add(B, 10)

changed = cv2.merge([B, G, R])

cv2.imshow("np", changed)
cv2.waitKey(0)



