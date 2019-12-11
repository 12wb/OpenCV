#!/usr/bin/env python3
# -*- coding:UTF8 -*-
"""
霍夫圆简检测
cv2.HoughCircles()，函数返回值为圆心坐标（x,y）圆半径R。
其函数原型为： HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) -> circles
重点参数解析：
    method：定义检测图像中圆的方法。目前唯一实现的方法是cv2.HOUGH_GRADIENT；
    dp：累加器分辨率与图像分辨率的反比。dp获取越大，累加器数组越小；
    minDist：检测到的圆的中心，（x,y）坐标之间的最小距离。如果minDist太小，则可能导致检测到多个相邻的圆。如果minDist太大，
    则可能导致很多圆检测不到；
    param1：用于处理边缘检测的梯度值方法；
    param2：cv2.HOUGH_GRADIENT方法的累加器阈值。阈值越小，检测到的圈子越多；
    minRadius：半径的最小大小（以像素为单位）；
    maxRadius：半径的最大大小（以像素为单位）。
"""
import cv2 as cv

def main():
    img = cv.imread('shape.png')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 230, 255, cv.THRESH_BINARY)
    edges = cv.Canny(thresh, 30, 90)
    cv.imshow('lines', thresh)
    cv.waitKey(0)
    circles = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, 1, 50, param1 = 100, param2 = 30, minRadius = 50,
                              maxRadius = 300)
    for x, y, r in circles[0]:
        cv.circle(img, (x, y), r, (0, 255, 0), 2, cv.LINE_AA)
        cv.circle(img, (x, y), 3, (255, 255, 255), -1, cv.LINE_AA)
    cv.imshow('lines', img)
    cv.waitKey(0)
    cv.destroyWindow('lines')


if __name__ == '__main__':
    main()
