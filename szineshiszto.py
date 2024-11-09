import cv2
import numpy as np
from matplotlib import pyplot as plt

R = cv2.imread("kepek/nature.jpg", 1)

colors = ('b', 'g', 'r')
plt.figure()
for i, color in enumerate(colors):
    hist = cv2.calcHist([R], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.title('Original RGB Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.xlim([0, 256])
plt.ylim([0, 2500])
plt.show()

HSV = cv2.cvtColor(R, cv2.COLOR_BGR2HSV)

HSV[:, :, 2] = cv2.equalizeHist(HSV[:, :, 2])

R_equalized = cv2.cvtColor(HSV, cv2.COLOR_HSV2BGR)

plt.figure()
for i, color in enumerate(colors):
    hist = cv2.calcHist([R_equalized], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.title('Equalized RGB Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.xlim([0, 256])
plt.ylim([0, 2500])
plt.show()

cv2.imshow('Original Image', R)
cv2.imshow('Equalized Image', R_equalized)
cv2.waitKey()
