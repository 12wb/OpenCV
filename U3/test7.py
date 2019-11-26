# 像素值相加计算
import cv2 as cv
import numpy as np
x = np.uint8([250])
y = np.uint8([10])
print(cv.add(x,y))  # 得到255
print(x+y)  # 得到4
# print(type(cv.add(x,y)))
dog1 = cv.imread('dog1.jpg')
dog2 = cv.imread('dog2.jpg')
dogcvadd = cv.add(dog1,dog2)
a = dog1 + dog2
cv.imshow('cvadd',dogcvadd)
cv.imshow('add',a)
cv.waitKey(0)
cv.destroyAllWindows()