import cv2
import numpy as np


img = cv2.imread('Resources/cards.png')
width, height = 250, 350
pts1 = np.float32([[84, 35], [212, 57], [57, 209], [181, 203]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(img, matrix , (width, height))
cv2.imshow('Cards', img)
cv2.imshow('Output', imgOutput)
cv2.waitKey(0)