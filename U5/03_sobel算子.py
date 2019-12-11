# coding=gbk
# sobel的算子优点是：计算简单，速度快，但不适应于纹理较为复杂的图像
import cv2 as cv
import numpy as np

def nothing(x):
    pass
cv.namedWindow('sobelx')
cv.namedWindow('sobely')

# 创建滑动条
cv.createTrackbar('xszie','sobelx',1,15,nothing)  # x轴上核的大小
cv.createTrackbar('ysize','sobely',1,15,nothing)  # y轴上核的大小
img = cv.imread('sudoku.jpg',0)
cv.imshow('img',img)

# 获得核的值
while True:
    kx = cv.getTrackbarPos('xsize','sobelx')
    ky = cv.getTrackbarPos('ysize','sobely')
    if (kx % 2==0):


        kx+=1
    if (ky % 2 == 0):
        ky+=1
    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=kx)    # 1代表x轴方向求偏导,0代表y轴方向不求偏导
    sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=ky)    # 0代表x轴方向不求偏导,1代表y轴方向求偏导
    sobelx = cv.convertScaleAbs(sobelx)    # 求绝对值
    sobely = cv.convertScaleAbs(sobely)
    # 图像混合
    sobel_xy = cv.addWeighted(sobelx,0.5,sobely,0.5,0)
    cv.imshow('sobelx',sobelx)
    cv.imshow('sobely',sobely)
    cv.imshow('sobel_xy',sobel_xy)
    k = cv.waitKey(24)&0XFF
    if chr(k) == 'q':
        break
cv.destroyAllWindows()

