import cv2
import cv2 as cv
import numpy as np
def main():
    img = cv.imread("kepek/virag.jpg", 1)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    h,s,v = cv.split(hsv_img)

    h1 = h >= 0
    h2 = h <= 20
    mask1 = np.bitwise_and(h1, h2)

    h3 = h >= 150
    h4 = h <= 179
    mask2 = np.bitwise_and(h3, h4)

    mask = np.bitwise_or(mask1, mask2)

    h[mask] += 110
    hsv_img = cv2.merge([h,s,v], 3)

    result = cv.cvtColor(hsv_img, cv.COLOR_HSV2BGR)

    cv.imshow("Original", img)
    cv.imshow("Result", result)
    cv.waitKey()




if __name__ == "__main__":
    main()