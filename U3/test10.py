import cv2 as cv
import numpy as np
img = cv.imread('rub00.jpg')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
# lower_green = np.array([35,43,46])
# upper_green = np.array([77,255,255])

# maskgreen = cv.inRange(hsv,lower_green,upper_green)
# green= cv.bitwise_and(img,img,mask=maskgreen)
#
# # 设置红色阈值
# lower_red =np.array([0,43,46])
# upper_red = np.array([10,255,255])
#
# lower_red_1 =np.array([170,43,46])
# upper_red_1 = np.array([180,255,255])
#
# maskred = cv.inRange(hsv,lower_red,upper_red)
# red = cv.bitwise_and(img,img,mask=maskred)

lower_yellow = np.array([20,43,46])
upper_yellow = np.array([34,255,255])
maskyellow = cv.inRange(hsv,lower_yellow,upper_yellow)
yellow = cv.bitwise_and(img,img,mask=maskyellow)
cv.imshow('r1',img)

lower_blue= np.array([100,43,46])
upper_blue = np.array([124,255,255])
maskblue = cv.inRange(hsv,lower_blue,upper_blue)
blue = cv.bitwise_and(img,img,mask=maskblue)
cv.imshow('r1',img)

#cv.imshow('r2',maskgreen)
#cv.imshow('r3',green)
cv.imshow('r4',blue)
cv.imshow('r5',yellow)
cv.waitKey(0)
