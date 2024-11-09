import cv2
import numpy as np
from szincsatornak import beolvasas

def main():
    img = cv2.resize(beolvasas(), dsize=(0,0), fx=0.75, fy=0.75)
    auto_blurred = cv2.boxFilter(img, -1, (7,7))
    gaussian_blurred = cv2.GaussianBlur(img, (7,7), 0)
    median_blurred = cv2.medianBlur(img, 7)

    cv2.imshow("Image", img)
    cv2.imshow("Box Blurred", auto_blurred)
    cv2.imshow("Gaussian Blurred", gaussian_blurred)
    cv2.imshow("Median Blurred", median_blurred)
    cv2.waitKey()

if __name__ == '__main__':
    main()