import cv2 as cv
import numpy as np
img = cv.imread('./noisy2.png',0)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
print(ret)
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)  # ret2为阈值
print(ret2)
blur = cv.GaussianBlur(img,(5,5),0)  # 降噪处理，高斯模糊
ret3,th3 = cv.threshold(blur,0,256,cv.THRESH_OTSU)
print(ret3)
cv.imshow('img1',th1)
cv.imshow('img2',th2)
cv.imshow('img4',blur)
cv.imshow('img3',th3)
cv.waitKey(0)
cv.destroyAllWindows()
# print(ret)
# print(ret2)
# print(th1)
# print(th2)