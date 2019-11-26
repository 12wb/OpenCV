import cv2 as cv
import numpy as np
img = cv.imread('./bkrc.jpg')
# 转换为灰度值
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(gray,200,255,cv.THRESH_BINARY_INV)
cv.namedWindow('OPEN')
def nothing(x):
    pass
cv.createTrackbar('ks','OPEN',2,25,nothing) # 2是滑动条的初始值，25为滑动条的最大值

while True:
    ks = cv.getTrackbarPos('ks','OPEN')
    # 取滑动条上的值
    if ks <= 1:
        ks+=1
    # 定义结构元，选取不同的参数进行设置。
    rectkernel = cv.getStructuringElement(cv.MORPH_RECT,(ks,ks))
    crosskernel = cv.getStructuringElement(cv.MORPH_CROSS,(ks,ks))
    ellipkernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(ks,ks))
    # 开运算操作
    rect = cv.morphologyEx(thresh,cv.MORPH_BLACKHAT,rectkernel)
    cross = cv.morphologyEx(thresh,cv.MORPH_BLACKHAT,crosskernel)
    ellip = cv.morphologyEx(thresh,cv.MORPH_BLACKHAT,ellipkernel)
    # 图片上写文字
    cv.putText(rect,'rect'+str(ks),(80,20),cv.FONT_HERSHEY_SIMPLEX,
               .65,(255,255,255),2)
    cv.putText(cross, 'cross'+str(ks),(80,20),cv.FONT_HERSHEY_SIMPLEX,
               .65,(255,255,255),2)
    cv.putText(ellip, 'ellip'+str(ks),(80,20),cv.FONT_HERSHEY_SIMPLEX,
               .65,(255,255,255),2)
    # 注意：ks是滑动条的值
    # 排成俩行俩列显示，这里对于垂直方向和水平方向都有要求
    h1 = np.hstack((thresh,rect))
    h2 = np.hstack((ellip,cross))
    # 先分别排成俩列再排成俩行
    cv.imshow('OPEN',np.vstack((h1,h2)))
    k = cv.waitKey(100)&0xff
    if chr(k) == 'q':
        break



