# 图片切片
import cv2 as cv
img_path = './test_alpha.png'
img = cv.imread(img_path,1)


'''
#img = cv.imread(img_path,0)
# cv.imshow('t1',img)
# cv.waitKey(0)''' # 显示灰色

print(img)
print("*"*40)
print(img[0,0])
print([1,1,1])
print(img.shape)
img.itemset((0,1,1),255)
print(img)
brimg = img.copy()
# 颜色通道反转，BGR到RGB
brimg = img[:,:,::-1]
print("BGR到RGB","*"*30)
cv.imshow('t1',brimg)
cv.waitKey(0)