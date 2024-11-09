import cv2
import numpy

def main():
    path = input("Elérési út:")
    img = cv2.imread(path, 1)

    sizeofKernel = 5
    blurred = cv2.GaussianBlur(img, (sizeofKernel, sizeofKernel), 1)

    unsharped = cv2.addWeighted(img, 1.5, blurred, -0.5, 0)

    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    vChannel = hsvImg[:, :, 2]
    equalizedV = cv2.equalizeHist(vChannel)
    hsvImg[:, :, 2] = equalizedV
    equalizedImg = cv2.cvtColor(hsvImg, cv2.COLOR_HSV2BGR)

    threshold_value = int(input("Adja meg a küszöbértéket (0-255 között): "))
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresholded_image = cv2.threshold(grayImg, threshold_value, 255, cv2.THRESH_BINARY)
    color_thresholded_image = cv2.bitwise_and(equalizedImg, equalizedImg, mask=thresholded_image)

    hue = int(input("Hue: "))
    saturation = float(input("Saturation: "))
    brightness = float(input("Value: "))
    hsv_image = cv2.cvtColor(color_thresholded_image, cv2.COLOR_BGR2HSV)
    hsv_image[..., 0] += numpy.uint8(hue)
    hsv_image[..., 1] += numpy.uint8(saturation)
    hsv_image[..., 2] += numpy.uint8(brightness)
    final_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    cv2.imshow("eredeti", img)
    cv2.imshow("elesitett kép", unsharped)
    cv2.imshow("kiegyenlitett", equalizedImg)
    cv2.imshow("kuszobolt", color_thresholded_image)
    cv2.imshow("vegkep", final_image)
    cv2.waitKey()
    cv2.destroyAllWindows()

    save_path = input("Mentési útvonal: ")
    cv2.imwrite(save_path, final_image, [int(cv2.IMWRITE_JPEG_QUALITY), 92])


if __name__ == "__main__":
    main()