# 显示图片函数
import cv2 as cv
img_path = './test.png'
img_bgr = cv.imread(img_path,1)  # 参数一：路径  参数二：颜色类型
img_gray = cv.imread(img_path,0)
cv.imshow('imgl',img_bgr)  # 参数一：窗口名称  参数二：图片
cv.imshow('imggray',img_gray)
cv.waitKey()  # 默认0，无限时的延时,等待键盘输入