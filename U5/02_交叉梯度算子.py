# coding=gbk
import numpy as np
import cv2 as cv

img = cv.imread('sudoku.jpg',0)
row,colum = img.shape
# print(row,colum)

# ����ͼƬ
imgf = np.copy(img)

# ָ������
imgf = imgf.astype('float')

# ��ԭͼ����һ��
roberts = np.zeros((row,colum))

# ʵ�����ӵ�����
for x in range(row-1):
    # ������
    for y in range(colum-1):
        # x���ϵ��ݶ�
        gx = abs(imgf[x,y]-imgf[x,y+1])   # abs��ʾ����ֵ
        # y����ݶ�
        gy = abs(imgf[x,y+1]-imgf[x+1,y])
        # ����
        roberts[x,y] = gx+gy

# ���ͼ��=ԭͼ+����
imgout = img+ roberts

# ��С��0��ֵ��Ϊ0������255��ֵ��Ϊ255��������ԭͼ����
imgout = np.where(imgout<0,0,np.where(imgout>255,255,imgout))
imgout = imgout.astype('uint8')
cv.imshow('imgout',imgout)
cv.waitKey(0)
