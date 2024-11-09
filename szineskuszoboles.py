import cv2
import numpy as np

img = cv2.imread("kepek/city.jpg", 1)

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_img)

saturation_threshold = int(input("Szaturáció küszöbértéke (0-255): "))

mask = s > saturation_threshold

high_saturation_img = np.zeros_like(img)
high_saturation_img[mask] = img[mask]

cv2.imshow("Eredeti kep", img)
cv2.imshow("Magas szaturacioju reszek", high_saturation_img)
cv2.waitKey()
cv2.destroyAllWindows()