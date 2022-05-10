import cv2
import numpy as np

kernel= np.ones((5,5),np.uint8)


img = cv2.imread('krishna.jpg')   # Actual Image
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Conversion of BGR to GRAY Scale image
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny =cv2.Canny(imgGray,250,250)
imgDilation=cv2.dilate(imgCanny,kernel,iterations=1)
imgErode=cv2.erode(imgDilation,kernel,iterations=1)

cv2.imshow('KRISHNA img',img)
cv2.imshow('KRISHNAs imgGray',imgGray)
cv2.imshow('KRISHNAs imgBlur',imgBlur)
cv2.imshow('KRISHNAs Canny',imgCanny)
cv2.imshow('KRISHNAs dilation',imgDilation)
cv2.imshow('KRISHNAs Erode',imgErode)

cv2.waitKey(0)