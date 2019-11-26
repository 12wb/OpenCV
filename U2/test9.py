import cv2 as cv
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter("OUTPUT.mp4",fourcc,30,(640,480))
while cap.isOpened():
    status,frame = cap.read()
    if status:
        out.write(frame)
        cv.imshow('bgr',frame)
        k = cv.waitKey(25)&0XFF
        if chr(k) =='q':
            break
cap.release()
out.release()
cv.destroyAllWindows()
