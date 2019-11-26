import cv2 as cv
import numpy as np
img = cv.imread('./color.jpg')

# 将RGB转为HSV用于颜色提取
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# 设置绿色阈值
lower_green = np.array([35,43,46])
upper_green = np.array([60,255,255])

# 提取颜色
green = cv.inRange(hsv,lower_green,upper_green)

#滤波
median = cv.medianBlur(green, 5)
cv.imshow('green',median)

# 创建矩形的内核
rectKernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))

# 闭运算
green = cv.morphologyEx(green,cv.MORPH_CLOSE,rectKernel)
cv.imshow('close',green)

# 开运算
green = cv.morphologyEx(green,cv.MORPH_OPEN,rectKernel)
cv.imshow('open',green)

cv.waitKey(0)
cv.destroyAllWindows()

