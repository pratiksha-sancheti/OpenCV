import cv2

img = cv2.imread("Resources/image1.jpg")
print(img.shape)

imgResize = cv2.resize(img, (500, 400))
print(imgResize.shape)

imgCropped = img[0:300, 100:300]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)
cv2.destroyAllWindows()