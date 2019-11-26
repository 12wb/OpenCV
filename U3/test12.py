import cv2 as cv
import numpy as np
img = cv.imread('./test.png')
img1 = cv.resize(img,None,fx=0.5,fy=0.5,interpolation=cv.INTER_CUBIC)
# print(img.shape)
# print(img1.shape)
cv.imshow('r1',img1)
cv.waitKey(0)
cv.destroyAllWindows()
