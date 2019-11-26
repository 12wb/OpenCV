# 视频文件转换为图片
import cv2
vc=cv2.VideoCapture("OUTPUT.mp4")
c=60
if vc.isOpened():
    rval,frame=vc.read()
else:
    rval=False
while rval:
    rval,frame=vc.read()
    cv2.imwrite('OUTPUT.mp4'+str(c)+'.jpg',frame)
    c=c+1
    cv2.waitKey(1)
