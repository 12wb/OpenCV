import cv2 as cv
import numpy as np
img = cv.imread('./01.jpg',1)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

edges = cv.Canny(gray,180,250)
cv.imshow('edges',edges)
contours,hierarchy = cv.findContours(edges,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

max_area_contour = cv.contourArea(contours[0])
max_cnt = None

# 寻找图像中最大轮廓
for cnt in contours:
    if cv.contourArea(cnt) > max_area_contour:
        max_cnt = cnt
        max_area_contour = cv.contourArea(cnt)

cv.drawContours(img,[max_cnt],0,(0,0,255),2,cv.LINE_AA)

x,y,ww,hh = cv.boundingRect(max_cnt)
roi = img[y:y+hh,x:x+ww]

# 计算旋转矩
ret = cv.minAreaRect(max_cnt)
(cx,cy),(w,h),ang = ret
print('旋转角度为:',ang)
if w > h:
    w,h =h,w
    ang += 90
# 图片尺寸放大
# drawing = np.zeros(roi.shape[0]+ ,)
# 图像倾斜校正
M = cv.getRotationMatrix2D((cx,cy),ang,1.0)
rotated = cv.warpAffine(roi,M,(roi.shape[1],roi.shape[0]))

cv.imshow('img',rotated)
cv.waitKey(0)
cv.destroyAllWindows()

