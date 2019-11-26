import cv2 as cv

# # 图片的路径cv2.imwrite('./step7/img/generator  .jpg',img)cv2.imwrite('./step7/img/generator.jpg',img)
img_path = './test_alpha.png'
# # 读入彩色图，注意OpenCv中颜色格式为BGR
img_bgr = cv.imread(img_path,-1)
print(img_bgr.ndim)
#  打印出形状
print(img_bgr.shape)
#  大小
print(img_bgr.size)
#  数据类型
print(img_bgr.dtype)
h, w, c = img_bgr.shape
print(h, w, c)
print("*" * 40)

print(img_bgr)
# print(img_bgr)

image = cv.imread('./test.png')
print(image)
print(image.shape)
print(image[520,499,:2])



import cv2
image = cv2.imread('test.png',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('test.png',image)


import matplotlib.pyplot as plt