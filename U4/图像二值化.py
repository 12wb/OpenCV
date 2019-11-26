import cv2 as cv
import numpy as np
img = cv.imread('./dog2.jpg',0)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(th1,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,10)  # 自适应
th3 = cv.adaptiveThreshold(th1,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,5)
th4 = cv.adaptiveThreshold(th1,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,0)
th5 = cv.adaptiveThreshold(th1,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,5)
cv.imshow('img1',img)
# cv.imshow('img1',th1)
# cv.imshow('img2',th2)
# cv.imshow('img3',th3)
cv.imshow('img3',th4)
cv.waitKey(0)
cv.destroyAllWindows()