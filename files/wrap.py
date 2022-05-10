import cv2  # Imported cv2 Library
import numpy as np

img=cv2.imread('R.jpg')
width,height= 350,373
#pt1=np.float32([[163,53],[330,85],[112,314],[283,357]])
#pt2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pt1,pt2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))
#cv2.imshow('Playing crads', img)
cv2.imshow('Heart card',imgOutput)
cv2.waitKey(0)
