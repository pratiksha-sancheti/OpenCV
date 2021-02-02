import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('image', img)
img[200:300, 200:300] = 255, 0, 0
cv2.imshow('image', img)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.imshow('image', img)
cv2.rectangle(img, (0, 0), (200, 300), (0, 0, 255), cv2.FILLED)
cv2.imshow('image', img)
cv2.circle(img, (250, 250), 30, (0, 255, 0), 5)
cv2.imshow('image', img)
cv2.putText(img, "Pratiksha", (300,300), cv2.FONT_ITALIC, 1, (0, 255, 150), 2)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()