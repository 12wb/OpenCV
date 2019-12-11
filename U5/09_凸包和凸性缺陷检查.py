#!/usr/bin/env python3
# -*- coding:UTF8 -*-

"""
函数原型如下：
    convexHull(points[, hull[, clockwise[, returnPoints]]]) -> hull
    重点参数解析：
        points:我们要传入的轮廓信息；
        hull：输出通常不需要；
        clockwise：方向标志，如果设置为 True输出的凸包是顺时针方向的。
        否则为逆时针方向。
        returnPoints：默认值为True。它会返回凸包上点的坐标。如果设置
        为 False就会返回与凸包点对应的轮廓上的点。
凸性缺陷分析
    convexityDefects(contour, convexhull[, convexityDefects]) -> convexityDefects
        参数解析：
        contour：一般就是轮廓检测函数findContours的输出
        convexhull：convexHull函数的输出，里面存储的是凸包信息、
        convexityDefects ：描述每一个凸包缺陷，实际上就是一系列点，这些点很难用。
        函数返回：[-1, 4]类型的list
            第一个名字叫做
            start_index,表示缺陷在轮廓上的开始处，他的值是开始点在函数第一个参数 contour 中的下标索引；

            Vec4i 第二个元素的名字叫
            end_index， 顾名思义其对应的值就是缺陷结束处在 contour 中的下标索引；

            Vec4i 第三个元素
            farthest_pt_index 是缺陷上距离轮廓凸包(convexhull)最远的点；

            Vec4i最后的元素叫
            fixpt_depth，fixpt_depth/256  表示了
            轮廓上以 farthest_pt_index 为下标的点到 轮廓凸包的(convexhull)的距离,以像素为单位。
"""

import cv2 as cv

if __name__ == "__main__":

    img = cv.imread('hand.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

    if (cv.__version__[0] == '4'):
        # 查找轮廓
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    else:
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # 画出凸包
    hull_cv = cv.convexHull(contours[0])
    cv.drawContours(img, [hull_cv], 0, (0, 0, 255), 2, cv.LINE_AA)

    # 检查一个曲线是不是凸的，返回True或Flase
    k = cv.isContourConvex(hull_cv)
    print(k)

    # 寻找凸缺陷
    # 画出缺陷上距离轮廓凸包(convexhull)最远的点
    hull = cv.convexHull(contours[0], returnPoints = False)
    defects = cv.convexityDefects(contours[0], hull)
    print(defects, defects.shape)
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        far = tuple(contours[0][f][0])
        cv.circle(img, far, 5, (0, 0, 255), -1)

    cv.imshow('img', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
