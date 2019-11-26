import cv2 as cv
import numpy as np


def nothing(x):
    pass


# 打开系统默认摄像头
img = cv.imread('./IMG/ga.png')

cv.namedWindow('windows',0)
cv.createTrackbar('d','windows',0,100,nothing)
cv.createTrackbar('sigmaColor','windows',0,200,nothing)
cv.createTrackbar('sigmaSpace','windows',0,200,nothing)
font = cv.FONT_HERSHEY_SIMPLEX

while True:
    frame = cv.resize(img, None, fx=.5, fy=.5, interpolation=cv.INTER_LINEAR)
    d = cv.getTrackbarPos('d', 'windows')
    sigmaColor = cv.getTrackbarPos('sigmaColor', 'windows')
    sigmaSpace = cv.getTrackbarPos('sigmaSpace', 'windows')
    # # kernel为正奇数
    # d = d if d % 2 == 1 else d + 1
    #
    # # 2D卷积运算
    # kernel = np.ones((d, d), np.float32) / (d *d)
    # filter2D = cv.filter2D(frame, -1, kernel)
    # filter2D = cv.putText(filter2D, "filter2D", (20, 20), font, .65, (255, 255, 255), 2)
    # 双边滤波
    bfilter = cv.bilateralFilter(frame, d,  sigmaColor, sigmaSpace)
    bfilter = cv.putText(bfilter, 'bfilter',  (20, 20), font, .65, (255, 255, 255), 2)


    cv.imshow('windows', bfilter)
    k = cv.waitKey(24) & 0xFF
    if chr(k) == 'q':
        break


# 颜色梯度和边界位置可以区别双边滤波   双边滤波同时使用空间高斯权重和灰度值相似性高斯权重。

