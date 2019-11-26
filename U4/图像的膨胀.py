import cv2 as cv
import numpy as np
# 二值化
img = cv.imread('./j.png', 0)
ret,img1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# 建立结构元，注意结构元不能出现0值,不建议默认为3*3
kernel = np.ones((10,10),np.float32)
dilation = cv.dilate(img,kernel)
cv.imshow('img',img)
cv.imshow('dilate',dilation)
cv.waitKey(0)
cv.destroyAllWindows()

# import cv2
# import numpy as np
#
#
# dilation = cv2.dilate(img, kernel)  # 膨胀
#
#
# # 3.开运算与闭运算
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 定义结构元素
#
# # 开运算
# img = cv2.imread('j_noise_out.bmp', 0)
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#
# cv2.imshow('opening', np.hstack((img, opening)))
# cv2.waitKey(0)
#
# # 闭运算
# img = cv2.imread('j_noise_in.bmp', 0)
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#
# cv2.imshow('closing', np.hstack((img, closing)))
# cv2.waitKey(0)
#
