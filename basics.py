import cv2
import numpy as np

##Reading Image

img = cv2.imread('Resources/abc.jpg')

cv2.imshow("Output", img)
cv2.waitKey(2000)

cv2.destroyWindow('Output')

#Reading video
cap = cv2.VideoCapture('Resources/test.mov')

while True:
    success, img = cap.read()
    if success == True:
        cv2.imshow("Video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):      #if pressed 'q',loop breaks and video playing is stopped
            break
    else:
        break
cap.release()
cv2.destroyWindow('Video')

##Reading Webcam
cap = cv2.VideoCapture(0)  #0 is ID for the camera
cap.set(3, 640)     #3-set width
cap.set(4, 480)     #4- set height
cap.set(10, 400)    #10-brightness

while True:
    success, img = cap.read()
    cv2.imshow("WebCam", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):      #if pressed 'q',loop breaks and video playing is stopped
        break


cap.release()
cv2.destroyWindow('WebCam')

img = cv2.imread("Resources/image1.jpg")
kernel = np.ones((5, 5), np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow("Original", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
cv2.destroyAllWindows()