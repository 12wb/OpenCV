# 实例1
'''import numpy as np
a = np.array([1,2,3])
print(a)

# def student(self,name,age,marks):

student = np.dtype([("name","str"),("age","int"),("marks","float32")])
print(student)

a = np.array([("wangwu",6,1.2),"lisi",7,1.0],dtype=student)
print(a)
'''

# 实例2
'''
import winsound
tone = {"1":532,"2":588,"3":600,"4":698,"5":784,"6":880,"7":988,"8":1098}
while True:
    winsound.Beep(tone[input()],500)'''


#检测摄像头
import  cv2 as cv
cap = cv.VideoCapture(0)
#0代表笔记本内置的摄像头
status,frame=cap.read()
#status返回布尔型，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False
#frame就是每一帧的图像，是个三维矩阵
fourcc= cv.VideoWriter_fourcc(*'XVID')
out1=cv.VideoWriter('out1.avi',fourcc,30,(640,480))
while status:
    status, frame = cap.read()
    #cv.line(frame,(0,0),(640,480),(255,0,0),5)
    cv.imshow('window',frame)
    out1.write(frame)
    cv.waitKey(20)

