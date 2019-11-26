'''
# 图像切割
import cv2 as cv
img = cv.imread('./plate01.jpg')
# cv.imshow('t1',img)
height,width = img.shape[:2]
# print(height,width)
dis = img[100:height-200,190:width-320]
cv.imshow('t2',dis)
cv.waitKey(0)
# print(img.shape)
'''

import cv2 as cv
img = cv.imread('./cat.jpg')
cv.imshow('t1',img)
cv.waitKey(0)
height,width = img.shape[:2]
dis = img[100:height-300,180:width-200]
cv.imshow('t2',dis)
cv.waitKey(0)




