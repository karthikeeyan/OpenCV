import cv2
facecascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('Pranitha-Subhash-Images-1.jpg')
imGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces= facecascade.detectMultiScale(imGray,1.1,4)
for (x,y,w,h) in faces :
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('Result',img)
cv2.waitKey(0)
