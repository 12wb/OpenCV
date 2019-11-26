import cv2 as cv
import numpy as np
img = cv.imread('./test.jpg',1)
b,g,r = cv.split(img)
cv.imshow('b1',b)
B2 = b*1.3
B2 = B2.astype(np.uint8)
B2 = B2 % 255
img1 = cv.merge((B2,g))
cv.imshow('img1',B2)
cv.waitKey(0)