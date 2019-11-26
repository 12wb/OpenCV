# 读取本地视频流
import cv2 as cv
cvpath = './test.mp4'
cap = cv.VideoCapture(cvpath)
cv.namedWindow("video", cv.WINDOW_NORMAL)
while cap.isOpened():
    status,frame = cap.read()
    if status:
        height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
        width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
        FPS = cap.get(5)
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        k = cv.waitKey(25)&0XFF
        key = chr(k)
        if key == "h":
            print(height,width,FPS)
        elif key == 'q':
            break
        cv.imshow("video",gray)
cv.destroyAllWindows()
