import cv2

img = cv2.imread('krishna.jpg')
print(img.shape) # Displyed in Height,width, and layers
Imgresizd=cv2.resize(img,(200,300))
crop=img[0:100,100:400]
cv2.imshow('resized',Imgresizd)
cv2.imshow('cropped',crop)

cv2.waitKey()