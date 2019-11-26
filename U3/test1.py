import cv2 as cv
import numpy as np
img = np.zeros((500,500,3),np.uint8)  # 定义一个画布
img1 = np.ones((500,500,3),np.uint8)*255  # 定义一个画布
# img1参数图像。 (0,0)参数pt1线段的第一个点。(499,499)param pt2线段的第二个点。(0,0,255)参数颜色线颜色。
# 5参数厚度线厚度。
# 绘制矩形
# cv.line(img,(0,0),(499,499),(255,255,255),5)
# cv.rectangle(img1,(255,0),(0,255),(0,255,0),1)
# cv.rectangle(img1,(25,0),(66,256),(46,210,255),2)
# cv.rectangle(img1,(258,0),(64,19),(0,0,255),3)
# cv.rectangle(img,(255,0),(0,255),(0,255,0),1)
# cv.circle(img,(255,255),100,(255,0,0),-1)  # 绘制蓝色圆，改为-1则填充为实心圆
# cv.circle(img,(255,255),150,(0,0,255),3)

# 绘制椭圆形
# cv.ellipse(img,(150,150),(70,40),30,0,360,(0,180,200),-1,cv.LINE_AA)
# cv.ellipse(img,(150,150),(90,50),30,0,360,(200,100,200),3,cv.LINE_AA)

'''
# 绘制多边形
# 准备一些顶点坐标
pts = np.array([[100,50],[200,300],[300,200],[400,200]],np.int32)
print(pts.shape)
# 画闭合多边形
cv.polylines(img1,[pts],True,(0,0,255),-1,cv.LINE_AA)
# 画不闭合多边形
cv.polylines(img,[pts],False,(0,255,0),3,cv.LINE_AA)
'''


# 在图像上绘制文字
font = cv.FONT_HERSHEY_COMPLEX
cv.putText(img,'learning OpenCV',(0,200),font,4,(255,255,255),cv.LINE_AA)
font1 = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img1,'BZG',(0,200),font1,4,(0,255,255),cv.LINE_AA)
cv.imshow('t1',img)
cv.imshow('t2',img1)
cv.waitKey(0)

