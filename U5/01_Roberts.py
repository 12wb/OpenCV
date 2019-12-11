# coding=gbk
# ���ķ�ʽ��ͨ���Խ���
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
        gx = abs(imgf[x+1,y]-imgf[x,y])   # abs��ʾ����ֵ
        # y����ݶ�
        gy = abs(imgf[x,y+1]-imgf[x,y])
        # ����
        roberts[x,y] = gx+gy

# ���ͼ��=ԭͼ+����
imgout = img+ roberts

# ��С��0��ֵ��Ϊ0������255��ֵ��Ϊ255��������ԭͼ����
imgout = np.where(imgout<0,0,np.where(imgout>255,255,imgout))
imgout = imgout.astype('uint8')
cv.imshow('imgout',imgout)
cv.waitKey(0)

#
# import cv2 as cv
# import numpy as np
#
# sudo = cv.imread('sudoku.jpg',cv.IMREAD_GRAYSCALE)
#
# height,width = sudo.shape[:2]
# # print(width,height)
#
# sharp = np.zeros((height,width))
# sharp = sharp.astype('float')
# roberts = np.zeros((height,width))
#
# for i in range(height-1):
#     for j in range(width-1):
#         sharp_x = abs(int(sudo[i+1][j+1]-int(sudo[i][j])))
#         sharp_y = abs(int(sudo[i][j+1]-int(sudo[i+1][j])))
#         sharp[i][j] = sharp_x+sharp_y
#
# result = sudo+sharp
# result = np.where(result > 255,255,result).astype('uint8')
#
# cv.imshow('sudo',sudo)
# cv.imshow('result',result)
# cv.waitKey(0)
# cv.destroyAllWindows()
