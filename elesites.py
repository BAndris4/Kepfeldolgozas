import cv2

img = cv2.imread("kepek/nature.jpg", 1)
img = cv2.resize(img, dsize=(0, 0), fx=0.15, fy=0.15)

noise_img = cv2.medianBlur(img, 3)

blurred_img = cv2.GaussianBlur(noise_img, (7,7), 1)
unsharped = cv2.addWeighted(noise_img, 2.5, blurred_img, -1.5, 0)



cv2.imshow("Image", img)
cv2.imshow("Unsharped", noise_img)
cv2.imshow("Final", unsharped)
cv2.waitKey()