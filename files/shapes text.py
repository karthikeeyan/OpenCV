import numpy as np
import cv2

img=np.zeros((512,512,3),np.uint8)
#print(img.shape)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,250),(0,0,255),2)
cv2.circle(img,(100,101),20,(255,255,255),2)
cv2.putText(img,'OpenCv',(200,300),cv2.FONT_HERSHEY_TRIPLEX,1,(255,0,0),2)
cv2.imshow('image',img)

cv2.waitKey()