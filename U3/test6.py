import cv2 as cv
import numpy as np
img = cv.imread('./cat.jpg')
# print(img)
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
cv.imshow('b1',b)                      
cv.imshow('g1',g)
cv.imshow('r1',r)
img5 = img
B = b*0.8
B = B.astype(np.uint8)
R = r * 1.1
R = R.astype(np.uint8)
R = R % 255
img5[:,:,0] = B
img5[:,:,2] = R
cv.imshow('t4',img)
cv.imshow('t5',img5)
cv.waitKey(0)
