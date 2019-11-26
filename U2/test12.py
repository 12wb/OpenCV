# 实现调色板的滑动条
import cv2 as cv
import numpy as np
img = np.ones((500,500,3),np.uint8) * 127
def nothing(x):
    pass
cv.namedWindow('t1',0)
cv.createTrackbar('B','t1',0,255,nothing)
cv.createTrackbar('G','t1',0,255,nothing)
cv.createTrackbar('R','t1',0,255,nothing)
while True:
    B = cv.getTrackbarPos('B','t1')
    G = cv.getTrackbarPos('G','t1')
    R = cv.getTrackbarPos('R','t1')
    img[:] = [B,G,R]
    cv.imshow('t1',img)
    k = cv.waitKey(25) & 0XFF
    if chr(k) == 'q':
        break
cv.destroyAllWindows()