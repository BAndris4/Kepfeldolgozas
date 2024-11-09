import cv2
import numpy as np
from matplotlib import pyplot as plt

R = cv2.imread("kepek/virag.jpg", 0)

hist_original = cv2.calcHist([R], [0], None, [256], [0, 256])
plt.figure()
plt.title('Original Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(hist_original)
plt.xlim([0, 256])
plt.ylim([0, 2500])
plt.show()

R_equalized = cv2.equalizeHist(R)

hist_equalized = cv2.calcHist([R_equalized], [0], None, [256], [0, 256])
plt.figure()
plt.title('Equalized Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(hist_equalized)
plt.xlim([0, 256])
plt.ylim([0, 2500])
plt.show()

cv2.imshow('Original Image', R)
cv2.imshow('Equalized Image', R_equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
