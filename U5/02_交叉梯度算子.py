# coding=gbk
import numpy as np
import cv2 as cv

img = cv.imread('sudoku.jpg',0)
row,colum = img.shape
# print(row,colum)

# 复制图片
imgf = np.copy(img)

# 指定类型
imgf = imgf.astype('float')

# 与原图保持一致
roberts = np.zeros((row,colum))

# 实现算子的运算
for x in range(row-1):
    # 列运算
    for y in range(colum-1):
        # x轴上的梯度
        gx = abs(imgf[x,y]-imgf[x,y+1])   # abs表示绝对值
        # y轴的梯度
        gy = abs(imgf[x,y+1]-imgf[x+1,y])
        # 算子
        roberts[x,y] = gx+gy

# 输出图像=原图+算子
imgout = img+ roberts

# 把小于0的值变为0，大于255的值变为255，否则是原图本身
imgout = np.where(imgout<0,0,np.where(imgout>255,255,imgout))
imgout = imgout.astype('uint8')
cv.imshow('imgout',imgout)
cv.waitKey(0)
