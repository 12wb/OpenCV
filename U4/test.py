'''
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(10)  # 如果使用x = range(5)会报错，因为它是一个迭代器不能进行直接的操作
y1 = x ** 2
y2 = x ** 3

fig,(ax1,ax2) = plt.subplots(1,2)
ax1.set_title('pingfang')
ax1.set_xlabel('x')
ax1.set_ylabel('x ** 2')
ax1.plot(x,y1)

ax2.set_title('lifang')
ax2.set_xlabel('x')
ax2.set_ylabel('x ** 3')
ax2.plot(x,y2)

plt.show()

# plt.title('Simple')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.plot(x,y)
# plt.show()
'''

# import cv2 as cv
#
# src = cv.imread('forCLA.png',cv.IMREAD_GRAYSCALE)
#
# dst1 = cv.equalizeHist(src)
# cla1 = cv.createCLAHE(clipLimit=5,tileGridSize=(8,8))
# dst2 = cla1.apply(src)
#
# cv.imshow('src',src)
# cv.imshow('dst1',dst1)
# cv.imshow('dst2',dst2)
#
# cv.waitKey(0)
# cv.destroyAllWindows()


import cv2 as cv
import numpy as np
img = cv.imread("./IMG/mouse.jpg")
# 均值滤波
blur = cv.blur(img,(5,5))
# 中值滤波
median = cv.medianBlur(img,5)  # 雪花点考虑中值滤波，斑点考虑双边滤波
# 高斯模糊
gblur = cv.GaussianBlur(img,(5,5),0)
# 双边滤波
bfilter = cv.bilateralFilter(img,-1,150,150)  # 阈值高于5的地方就擦掉
cv.imshow('img1',blur)
cv.imshow('median',median)
cv.imshow('gblur',gblur)
cv.imshow('bfilter',bfilter)
cv.waitKey(0)
cv.destroyAllWindows()
