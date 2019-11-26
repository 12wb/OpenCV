# 视频文件的读写
import cv2 as cv
cap = cv.VideoCapture(0)  # 0为内置摄像头
cv.namedWindow('capl')
while cap.isOpened():
    status,frame = cap.read()
    if status:
        # 高度
        height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
        # 宽度
        width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
        FPS = cap.get(cv.CAP_PROP_FPS)
        k = cv.waitKey(25)&0xFF
        key = chr(k)
        if key == 'h':
            print(height,width)
        elif key == 'q':
            break
        cv.imshow('capl',frame)
cv.destroyAllWindows()