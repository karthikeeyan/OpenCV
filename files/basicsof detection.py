import cv2

front_face_detector=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

image=cv2.imread('venv\Images\group.jpg')

gray_image= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
face=front_face_detector.detectMultiScale(gray_image)
print(face)

for x,y,w,h in face:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),3)

cv2.imshow('Group',image)
cv2.waitKey()
#cv2.imshow('pranitha',gray_image)
#cv2.waitKey()
