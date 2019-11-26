import cv2 as cv
import numpy as np
img = cv.imread("./IMG/mouse.jpg")
# 自定义核
ke1 = np.ones((5,5),np.float32)/25
ke2 = np.array([[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0]])/9
ke3 = np.array([[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0],[0,1,0,1,0],[1,0,0,0,1]])/9
dst1 = cv.filter2D(img,-1,ke1)
dst2 = cv.filter2D(img,-1,ke2)
dst3 = cv.filter2D(img,-1,ke3)
cv.imshow('img0',img)
cv.imshow('img',dst1)
cv.imshow('img1',dst2)
cv.imshow('img2',dst3)
cv.waitKey(0)
cv.destroyAllWindows()
