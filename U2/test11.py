# 实时视频转换为图片并保存
import cv2 as cv
import datetime
cap = cv.VideoCapture(0)
while cap.isOpened():
    status, frame = cap.read()
    if status:
        k = cv.waitKey(1) & 0XFF
        key = chr(k)
        if key == 'q':
            break
        else:
            currtime=datetime.datetime.now()
            timestr = datetime.datetime.strftime(currtime, '%Y%m%d_%H&M%S')
            print(timestr)
            fileframe = 'D:\\Pycharm\\OpenCV\\U2\\BiZhiGang\\'+timestr+'.jpg'
            cv.imwrite(fileframe, frame)
        cv.imshow('video', frame)
cv.destroyAllWindows()
