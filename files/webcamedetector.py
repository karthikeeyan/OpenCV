import cv2

front_face_detector=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
while True:
    sucess, frame = video.read()
    if sucess== True:
        gray_image= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face=front_face_detector.detectMultiScale(gray_image)
        for x,y,w,h in face :
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        cv2.imshow('WEBCAME',frame)

        if cv2.waitKey(1) &  0xFF == ord('q'):
            break
    else:
        print('Video Completed/stopped')

