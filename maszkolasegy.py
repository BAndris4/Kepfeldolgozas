import cv2
import numpy


def main():
    R = cv2.imread("kepek/nature.jpg", 1)
    R = cv2.resize(R,(0,0),fx=0.125,fy=0.125)
    orig = R

    R = cv2.cvtColor(R, cv2.COLOR_RGB2HSV)
    H, S, V = cv2.split(R)

    H1 = H >= 100
    H2 = H <= 120
    mask = numpy.bitwise_and(H1, H2)
    H[mask] += 50
    R = cv2.merge([H, S, V], 3)
    R = cv2.cvtColor(R, cv2.COLOR_HSV2RGB)
    cv2.imshow("Modified", R)
    cv2.imshow("Original", orig)
    cv2.waitKey()

if __name__=="__main__":
    main()