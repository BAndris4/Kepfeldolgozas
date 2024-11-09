import cv2

img = cv2.imread("kepek/city.jpg", 0)
equalized_img = cv2.equalizeHist(img)
cv2.imshow("Image", img)
cv2.imshow("Equalized", equalized_img)
cv2.waitKey()