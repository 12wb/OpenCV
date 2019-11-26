import numpy as np
import cv2 as cv
imgpach='./test.png'
img1=cv.imread(imgpach,1)
img1[:,:,2]=0
img2=cv.imread(imgpach,cv.IMREAD_GRAYSCALE)
cv.imshow('gray1',img2)
cv.imshow('bgrl',img1)
cv.waitKey(0)
