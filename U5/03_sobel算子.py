# coding=gbk
# sobel�������ŵ��ǣ�����򵥣��ٶȿ죬������Ӧ�������Ϊ���ӵ�ͼ��
import cv2 as cv
import numpy as np

def nothing(x):
    pass
cv.namedWindow('sobelx')
cv.namedWindow('sobely')

# ����������
cv.createTrackbar('xszie','sobelx',1,15,nothing)  # x���Ϻ˵Ĵ�С
cv.createTrackbar('ysize','sobely',1,15,nothing)  # y���Ϻ˵Ĵ�С
img = cv.imread('sudoku.jpg',0)
cv.imshow('img',img)

# ��ú˵�ֵ
while True:
    kx = cv.getTrackbarPos('xsize','sobelx')
    ky = cv.getTrackbarPos('ysize','sobely')
    if (kx % 2==0):


        kx+=1
    if (ky % 2 == 0):
        ky+=1
    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=kx)    # 1����x�᷽����ƫ��,0����y�᷽����ƫ��
    sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=ky)    # 0����x�᷽����ƫ��,1����y�᷽����ƫ��
    sobelx = cv.convertScaleAbs(sobelx)    # �����ֵ
    sobely = cv.convertScaleAbs(sobely)
    # ͼ����
    sobel_xy = cv.addWeighted(sobelx,0.5,sobely,0.5,0)
    cv.imshow('sobelx',sobelx)
    cv.imshow('sobely',sobely)
    cv.imshow('sobel_xy',sobel_xy)
    k = cv.waitKey(24)&0XFF
    if chr(k) == 'q':
        break
cv.destroyAllWindows()

