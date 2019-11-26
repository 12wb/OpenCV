import cv2 as cv
import numpy as np

img = cv.imread('./plate02.png',0)

# 二值化
ret,img1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# 建立结构元，注意结构元不能出现0值,不建议默认为3*3
kernel = np.ones((3,3),np.float32)
# 腐蚀操作   去除白噪声，断连
erosion = cv.erode(img1,kernel,iterations=1)
# 膨胀操作
dilation = cv.dilate(img,kernel)
# iterations=1代表操作一次

cv.imshow('img',img)
cv.imshow('erode',erosion)
cv.imshow('dilate',dilation)
cv.waitKey(0)
cv.destroyAllWindows()

# OpenCV定义的结构元素
# kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
# 腐蚀图像
# eroded = cv.erode(img,kernel)
# 显示腐蚀后的图像
# cv.imshow("Eroded Image",eroded)

# # 膨胀图像
# dilated = cv.dilate(img, kernel)
# # 显示膨胀后的图像
# cv.imshow("Dilated Image", dilated);
# # 原图像
# cv.imshow("Origin", img)
#
# # NumPy定义的结构元素
# NpKernel = np.uint8(np.ones((3, 3)))
# Nperoded = cv.erode(img, NpKernel)
# # 显示腐蚀后的图像
# cv.imshow("Eroded by NumPy kernel", Nperoded);

# cv.waitKey(0)
# cv.destroyAllWindows()



'''
import cv2
import numpy as np

# 1.腐蚀与膨胀
img = cv2.imread('j.png', 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel)  # 腐蚀
dilation = cv2.dilate(img, kernel)  # 膨胀

cv2.imshow('erosion/dilation',np.hstack((img,erosion,dilation)))
cv2.waitKey(0)


# 2.定义结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))  # 矩形结构
print(kernel)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))  # 椭圆结构
print(kernel)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))  # 十字形结构
print(kernel)

# 3.开运算与闭运算
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))  # 定义结构元素

# 开运算
img = cv2.imread('j_noise_out.bmp',0)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

cv2.imshow('opening',np.hstack((img,opening)))
cv2.waitKey(0)

# 闭运算
img = cv2.imread('j_noise_in.bmp',0)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE, kernel)

cv2.imshow('closing',np.hstack((img,closing)))
cv2.waitKey(0)


# 4.形态学梯度
img = cv2.imread('school.bmp', 0)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('morphological gradient', np.hstack((img, gradient)))
cv2.waitKey(0)


# 5.顶帽
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('top hat', np.hstack((img, tophat)))
cv2.waitKey(0)


# 6.黑帽
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('black hat', np.hstack((img, blackhat)))
cv2.waitKey(0)
'''