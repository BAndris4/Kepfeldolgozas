import cv2
import numpy as np

def main():
    img = cv2.imread("kepek/nature.jpg", 1)
    img = cv2.resize(img, dsize=(0,0), fx=0.1, fy=0.1)
    cv2.imshow('Original Image', img)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    '''lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    increased_hue = hsv[:, :, 0] + 100
    image_increased = cv2.merge([increased_hue, hsv[:, :, 1], hsv[:, :, 2]])
    image_increased = cv2.cvtColor(image_increased, cv2.COLOR_HSV2BGR)

    output = np.zeros_like(img)
    output[mask > 0] = image_increased[mask > 0]
    output[mask == 0] = img[mask == 0]'''

    mask = cv2.inRange(hsv, (0, 50, 100), (180, 170, 200))
    condition = (img[..., 0] <= 2 * 100)
    mask = mask & condition.astype(np.uint8) * 255

    output = np.zeros_like(img)
    output[mask > 0] = img[mask > 0]

    cv2.imshow("Maszkolt", output)

    cv2.waitKey(0)

if __name__ == "__main__":
    main()
