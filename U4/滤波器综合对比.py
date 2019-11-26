import cv2 as cv
import numpy as np
def nothing(x):
    pass
cap = cv.VideoCapture(0)
cv.namedWindow('windows')
cv.createTrackbar('ks','windows',3,31,nothing)
font = cv.FONT_HERSHEY_SIMPLEX
while cap.isOpened():
    ret,frame = cap.read()
    frame = cv.resize(frame,None,fx=.5,fy=.5,interpolation=cv.INTER_LINEAR)
    ks = cv.getTrackbarPos('ks','windows')
    # 保证ks为正奇数
    ks = ks if ks%2==1 else ks+1
    # 2D卷积运算
    kernel = np.ones((ks,ks),np.float32)/(ks*ks)
    filter2D = cv.filter2D(frame,-1,kernel)  # 填-1所有计算由核来完成
    filter2D = cv.putText(filter2D,'filer2d',(20,20),font,0.65,(255,255,255),2)
    # 均值模糊
    blur = cv.blur(frame,(ks,ks))
    blur = cv.putText(blur,'blur',(20,20),font,0.65,(255,255,255),2)
    # 高斯模糊
    gblur = cv.GaussianBlur(frame,(ks,ks),0)
    gblur = cv.putText(gblur,'gblur',(20,20),font,0.65,(255,255,255),2)
    # 中值滤波
    medianblur = cv.medianBlur(frame,ks,0)  # 需要填的正奇数
    medianblur = cv.putText(medianblur,'medianblur',(20,20),font,0.65,(255,255,255),2)
    # 双边滤波
    bfilter = cv.bilateralFilter(frame,-1,2*ks,int(0.7*ks))
    bfilter = cv.putText(bfilter,'bfilter',(20,20),font,0.65,(255,255,255),2)
    hs1 = np.hstack((frame,blur,filter2D))
    hs2 = np.hstack((gblur,medianblur,bfilter))
    vs = np.vstack((hs1,hs2))
    cv.imshow('windows',vs)
    k = cv.waitKey(25)
cv.destroyAllWindows()

