# 它会用二阶的导数取代一阶的导数
import cv2 as cv
import numpy as np
img = cv.imread('./apple.jpg')
scharrx = cv.Scharr(img,cv.CV_64F,1,0)
scharry = cv.Scharr(img,cv.CV_64F,0,1)
scharrx = cv.convertScaleAbs(scharrx)  # 归一化的处理
scharry = cv.convertScaleAbs(scharry)
scharr_xy = cv.addWeighted(scharrx,.5,scharry,.5,0)
cv.imshow('img',img)
cv.imshow('img1',scharrx)
cv.imshow('img2',scharry)
cv.imshow('img3',scharr_xy)
cv.waitKey(0)
cv.destroyAllWindows()

print(pip.pep425tags.get_supported())