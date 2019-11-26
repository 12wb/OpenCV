# 使用摄像头进行颜色转换
import cv2 as cv
import numpy as np
cv.namedWindow('color',0)
def nothing(x):
    pass
cv.createTrackbar("HMAX","color",0,180,nothing)
cv.createTrackbar("HMIN","color",0,180,nothing)
cap = cv.VideoCapture(0)
while cap.isOpened():  # 判断摄像头是否打开
    ret,frame = cap.read()  # 状态，帧
    if ret:
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower = cv.getTrackbarPos("HMIN",'color')
        upper = cv.getTrackbarPos("HMAX",'color')
        hsvmin = np.array([lower,60,60])
        hsvmax = np.array([upper,255,255])
        mask = cv.inRange(hsv,hsvmin,hsvmax)  # 建立掩模
        img = cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow('color',img)
        cv.waitKey(25)
    else:
        break
cap.release()
cv.destroyAllWindows()



