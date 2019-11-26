# 图片通道合并
import cv2 as cv
import numpy as np
img = cv.imread('./cat.jpg')
if img is None:
    raise Exception('文件路径有误')
if len(img.shape) < 3:
    raise Exception('图片通道不够')

b,g,r = cv.split(img)
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)
R = r * 1.1
R = R.astype(np.uint8)
R = R % 255
G = g*0.9
G = G.astype(np.uint8)
img2 = cv.merge((b,G,R))
cv.imshow('r1',img)
cv.imshow('g2',img2)
cv.waitKey(0)