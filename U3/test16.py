import cv2 as cv
img = cv.imread('./test.png',0)
ret,thresh_binary = cv.threshold(img,127,255,cv.THRESH_BINARY)
# print

ret_inv,thresh_binary_inv = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)

cv.imshow('thresh_binary',thresh_binary)
cv.imshow('thresh_binary_inv',thresh_binary_inv)
cv.waitKey(0)
