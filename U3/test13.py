# 图片的平移
import cv2 as cv
import numpy as np
img = cv.imread('./test.png')
# 原图的高度
row,cols = img.shape[:2]
# print(row,cols)
#M = np.float32([[0.25,0,3*row/8],[0,0.25,3*cols/8]])  # 第一个1代表x0，第二个1代表y0
#dst = cv.warpAffine(img,M,(row,cols),borderValue=(255,0,255))  # 平移
M2 = cv.getRotationMatrix2D((row/2,cols/2),30,0.6)  # 缩小0.6倍，旋转30°
dst = cv.warpAffine(img,M2,(row,cols))
dst2 = cv.rotate(dst,cv.ROTATE_90_CLOCKWISE)
cv.imshow('r1',dst)
cv.imshow('r2',dst2)
cv.waitKey(0)