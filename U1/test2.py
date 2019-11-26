'''
# 实例3
import numpy as np
# a现只有一个维度
a = np.arange(24)
print(a)
print(a.ndim)
# 现在调整其大小
# b现有三个维度
b = a.reshape(3,4,2)
print(b.ndim)


# 实例4
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a.shape)


# 实例5
import numpy as np
# 数组的dtype为int8(一个字节)
x = np.array([1,2,3,4,5],dtype=np.int8)
print(x.itemsize)

# dtype现在为float64(八个字节)
y = np.array([1,2,3,4,5],dtype=np.float64)
print(y.itemsize)


# 实例6
import numpy as np
# 默认为浮点数
x = np.ones(5)
print(x)

# 自定义类型
x = np.ones([2,2],dtype=int)
print(x)'''

'''
import numpy as np
import cv2 as cv
img = np.zeros((3,3), dtype=np.uint8)
print(img)
print("\n")
img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)  # 转换为BGR格式
print(img)
print(img.shape)'''


import cv2 as cv
import numpy as np
img = cv.imread("test_alpha.png")
img[:,:,0] = 0  # 冒号代表所有，第一个冒号代表行，第二个冒号代表列，0代表BGR
cv.imshow('windows',img)
cv.waitKey(0)