# Basics of images
import cv2  # Imported cv2 Library

img = cv2.imread('krishna.jpg')  # To read the image of our choice
cv2.imshow('KRISHNA', img)  # To display the image
cv2.waitKey()  # Delay the image image for a while

# Basics of videos

#

video= cv2.VideoCapture(0)
video.set(3,640)
video.set(4,480)
video.set(10,100)
while True :
    success, image=video.read()
    cv2.imshow("video",image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break