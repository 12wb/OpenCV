#!/usr/bin/env python3
# -*- coding:UTF8 -*-

"""
    学习使用函数setMouseCallback()监听鼠标事件
    在我的系统中所支持的一些事件
        ['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 
        'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 
        'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 
        'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 
        'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK',
        'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 
        'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 
        'EVENT_MOUSEWHEEL', 'EVENT_RBUTTONDBLCLK', 
        'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']

        中文解释
        cv2.EVENT_MOUSEMOVE    0   鼠标移动事件
        cv.EVENT_LBUTTONDOWN   1   鼠标左键按下事件
        cv.EVENT_RBUTTONDOWN   2   鼠标右键按下事件
        cv.EVENT_MBUTTONDOWN   3   鼠标中键按下事件
        cv.EVENT_LBUTTONUP     4   鼠标左键释放事件
        cv.EVENT_RBUTTONUP     5   鼠标右键释放事件
        cv.EVENT_MBUTTONUP     6   鼠标中键释放事件
        cv.EVENT_LBUTTONBLCLK  7   鼠标左键双击事件
        cv.EVENT_RBUTTONBLCLK  8   鼠标右键双击事件
        cv.EVENT_MBUTTONBLCLK  9   鼠标中键双击事件
        cv.EVENT_MOUSEWHEEL    10  滑动滚轮上下滚动
        cv.EVENT_MOUSEHWHEEL   11  滑动滚轮左右滚动
"""

import cv2 as cv
import numpy as np

ox = 0
oy = 0

# 创建一张灰白色的图片
img = np.ones((500, 500, 3), np.uint8) * 127


# 回调函数，在回调函数中处理
def draw_circle(event, x, y, flags, param):
    # global 修饰的字段，表示使用全局变量
    global img
    global ox, oy

    # 鼠标左键双击
    if event == cv.EVENT_LBUTTONDBLCLK:
        img = np.ones((500, 500, 3), np.uint8) * 127
        cv.circle(img, (x, y), 150, (0, 255, 0), -1, cv.LINE_AA)
    # 鼠标移动事件
    elif event == cv.EVENT_MOUSEMOVE:
        cv.line(img, (ox, oy), (x, y), (255, 255, 255), 3, cv.LINE_AA)
        ox, oy = x, y


# 创建一个窗体并为鼠标事件绑定监听回调函数
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while True:
    cv.imshow('image', img)
    k = cv.waitKey(25) & 0xFF
    if chr(k) == 'q':
        break
