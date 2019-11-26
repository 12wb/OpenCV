import cv2 as cv
import  numpy as np
img = np.ones((920,800,3),np.uint8)
cv.line(img,(100,400),(400,400),(0,0,255),4)
cv.line(img,(250,250),(250,550),(255,255,255),4)
cv.rectangle(img,(100,250),(400,550),(0,0,255),3)
cv.rectangle(img,(150,280),(350,520),(255,0,255),3)
cv.rectangle(img,(200,320),(300,480),(255,0,0),3)
cv.circle(img,(250,400),150,(0,255,0),3)
cv.circle(img,(250,400),100,(258,220,255),3)
cv.circle(img,(250,400),50,(156,180,233),3)
cv.ellipse(img,(250,100),(20,30),90,0,180,(168,255,255),-1,cv.LINE_AA)
cv.ellipse(img,(250,100),(25,35),270,0,90,(255,0,255),2,cv.LINE_AA)
cv.ellipse(img,(250,100),(25,35),270,0,180,(255,0,0),-1,cv.LINE_AA)
cv.ellipse(img,(250,100),(90,60),0,0,360,(255,255,0),3,cv.LINE_AA)
cv.ellipse(img,(250,100),(35,50),270,0,180,(0,255,200),3,cv.LINE_AA)

pts=np.array([[510,300],[700,250],[600,550],[790,500]],np.int32)
cv.polylines(img,[pts],True,(255,0,255),3)
cv.polylines(img,[pts],False,(255,0,255),3)



font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,"BiZhiGang",(0,700),font,3,(0,0,255),cv.LINE_AA)
cv.putText(img,'49',(500,200),font,3,(255,255,255),cv.LINE_AA)
cv.imshow('img',img)
cv.waitKey(0)
