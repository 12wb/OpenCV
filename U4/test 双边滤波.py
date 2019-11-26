import numpy as np
import cv2 as cv

def nothing(x):
    pass

img = cv.imread('./IMG/img8.jpg')
cv.namedWindow('windows',0)
cv.createTrackbar('d','windows',0,100,nothing)
cv.createTrackbar('sigmaColor','windows',0,200,nothing)
cv.createTrackbar('sigmaSpace','windows',0,200,nothing)
font = cv.FONT_HERSHEY_SIMPLEX

while True:
    frame = cv.resize(img, None, fx=.5, fy=.5, interpolation=cv.INTER_LINEAR)
    d = cv.getTrackbarPos('d', 'windows')
    sigmaColor = cv.getTrackbarPos('sigmaColor', 'windows')
    sigmaSpace = cv.getTrackbarPos('sigmaSpace', 'windows')

    bfilter = cv.bilateralFilter(frame, d, sigmaColor, sigmaSpace)
    bfilter = cv.putText(bfilter,'bfilter',(20,20),font,.65,(255,255,255),2)

    cv.imshow('windows',bfilter)
    k = cv.waitKey(24) & 0xFF
    if chr(k) == 'q':
        break

