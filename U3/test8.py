import cv2 as cv
import numpy as np
meixi = cv.imread('meixi.jpg')
opencv = cv.imread('opencv.png')
print(meixi.shape)
print(opencv.shape)
h,w = opencv.shape[:2]
print(h,w)
roi = meixi[:h,:w]
cv.imshow('r1',roi)

# cvadd = cv.add(roi,opencv)
# cv.imshow('r2',cvadd)
cvgray = cv.cvtColor(opencv,cv.COLOR_BGR2GRAY)  # 进行图像灰度化
ret,mask = cv.threshold(cvgray,200,255,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask) # 非运算
img1_bg = cv.bitwise_and(roi,roi,mask=mask)
# roi中非零值的地方会保留
cv.imshow('imgl_bg',img1_bg)
img1_fg = cv.bitwise_and(opencv,opencv,mask=mask_inv)
dst = cv.add(img1_fg,img1_bg)
meixi[:h,:w] =  dst
cv.imshow('r1',meixi)
cv.imshow('r2',cvgray)
cv.imshow('r3',mask)
cv.imshow('r4',mask_inv)
cv.imshow('r6',img1_bg)
cv.imshow('r5',img1_fg)
cv.imshow('r7',dst)
cv.waitKey(0)
