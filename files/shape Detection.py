import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
def getcontours(img):
    contour,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for i in contour:
        area=cv2.contourArea(i)
        print(area)
        if area>50:
            cv2.drawContours(img,i,-1,(255,0,0),3)
            perimeter= cv2.arcLength(i,True)
            approx=cv2.approxPolyDP(i,0.02*perimeter,True)
            print(len(approx))
            objcor=len(approx)
            x,y,w,h=cv2.boundingRect(approx)
            if objcor == 3: objectType='Tri'
            elif objcor==4 :
                aspectRatio=w/float(h)
                if aspectRatio>0/95 and aspectRatio <1.05: objectType = 'square'
                else : objectType = 'Rectangle'
            elif objcor >4 : objectType="Circle"
            else: objectType= 'None'


            cv2.rectangle(imagContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imagContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,255,255),2)







img=cv2.imread('shapes.jpg')
img=cv2.resize(img,(450,450))
#img=cv2.resize(img,(450,450))

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imagecanny=cv2.Canny(imgBlur,50,50)
imagContour=img.copy()

imageblank=np.zeros_like(img)
imagesstak=stackImages(0.5,([img,imgBlur,imgGray],[imagecanny,imagContour,imageblank]))
getcontours(imagecanny)

cv2.imshow('Stacked Shapes',imagesstak)
#cv2.imshow('imgGray',imgGray)
#cv2.imshow('imgBlur',imgBlur)

cv2.waitKey(0)