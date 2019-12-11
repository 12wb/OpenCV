import cv2 as cv
import numpy as np
img = cv.imread('bmx.jpg')
blur = cv.GaussianBlur(img,(5,5),-5,-5)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 大津算法
#ret,threshold = cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

ret,g = cv.threshold(gray,180,255,cv.THRESH_BINARY) # ret阈值，g图片
edges = cv.Canny(g,120,200)

# 霍夫变换
lines = cv.HoughLines(edges,1,np.pi/180,135)
# print(lines)

# 循环
for line in lines:
    for rho,theta in line:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0+1000*(a))
        x2 = int(x0-1000*(-b))
        y2 = int(y0-1000*(a))
        cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv.imshow('img',g)
cv.imshow('img1',edges)
cv.imshow('lines',img)
cv.waitKey(0)
