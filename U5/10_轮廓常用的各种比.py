#!/usr/bin/env python3
# -*- coding:UTF8 -*-

"""
轮廓的性质
"""
import cv2 as cv
import numpy as np

if __name__ == "__main__":
    # # 生成一张黑色背景的图像
    #   img = np.zeros((512, 512, 3), np.uint8)

    #   #添加一个矩形
    #   img[100:300, 100:400, :3] = 255
    img1 = cv.imread('star.png')
    img=cv.resize(img1,None,fx=0.5,fy=0.5,interpolation=cv.INTER_CUBIC)


    # 灰度a
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # 简单阈值的二值化
    ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

    if (cv.__version__[0] == '4'):
        # 查找轮廓
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    else:
        _, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]

    # 长宽比
    x, y, w, h = cv.boundingRect(cnt)
    aspect_ratio = w / h
    print('长宽比：{:.2f}'.format(aspect_ratio))
    img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2, cv.LINE_AA)

    # 轮廓面积与边界矩形比：
    area = cv.contourArea(cnt)
    x, y, w, h = cv.boundingRect(cnt)
    rect_area = w * h
    extent = float(area) / rect_area
    print('轮廓面积与边界矩形比：{:.2f}'.format(extent))

    # 轮廓面积和凸包面积比：
    area = cv.contourArea(cnt)
    hull = cv.convexHull(cnt)
    hull_area = cv.contourArea(hull)
    solidity = float(area) / hull_area
    print('轮廓面积和凸包面积比:{:.2f}'.format(solidity))
    cv.drawContours(img, [hull], 0, (0, 0, 255), 2, cv.LINE_AA)

    # 与轮廓面积相等圆直径：
    area = cv.contourArea(cnt)
    equi_diameter = np.sqrt(4 * area / np.pi)
    print('与轮廓面积相等圆直径：{:.2f}'.format(equi_diameter))

    cv.imshow("Output", img)

    cv.waitKey(0)
    cv.destroyAllWindows()
