import cv2 as cv
img = cv.imread('hand.jpg')
img = cv.resize(img,(400,400),interpolation=cv.INTER_CUBIC)
# 转为灰度图
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 进行二值化处理
ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# 返回的两个值
# 检测轮廓
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# print(contours)
# print(hierarchy)
cv.drawContours(img, contours, -1, (0, 0, 255), 3)

cv.imshow("img", img)
cv.imshow('binary',binary)
cv.waitKey(0)
