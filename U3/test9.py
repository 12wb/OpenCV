import cv2 as cv
flags = [i for i in dir(cv) if i.startswith('COLOR_')]  # 计算以COLOR_开头的有多少个
print(flags)
print(len(flags))