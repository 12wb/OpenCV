import cv2 as cv
sea = cv.imread('sea.jpg')
sun = cv.imread('sun.jpg')
img1 = cv.addWeighted(sea,0.8,sun,0.2,1)
img2 = cv.addWeighted(sun,0.8,sea,0.2,1)
cv.imshow('a',sea)
cv.imshow('b',sun)
cv.imshow('a1',img1)
cv.imshow('b1',img2)
cv.waitKey(0)

