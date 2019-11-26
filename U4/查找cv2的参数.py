from cv2 import cv2

for i in dir(cv2):
    if i.startswith("COLOR"): # "COLOR" 输入 你需要查找的元素 里面含有的部分
        print(i)