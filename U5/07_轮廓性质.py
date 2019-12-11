import cv2 as cv
img = cv.imread('02.png')
gray = cv.cvtColor(img,cv.COLOR_BGRA2GRAY)
#blured=cv.blur(gray,(3,3)) #平滑
ret,thresh =cv.threshold(gray,127,255,cv.THRESH_BINARY)
c,h=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
#绘制轮廓
cv.drawContours(img,c,1,(255,0,0),2,8)
cv.drawContours(img,c,2,(0,255,255),2,8)
c1 = c[1]
c0 = c[0]
M = cv.moments(c1)
print(M)
cx = int(M["m10"]/M["m00"])
cy = int(M["m01"]/M["m00"])
cv.circle(img,(cx,cy),1,(0,255,0),8)
cv.imshow('t1',gray)
cv.imshow('t2',img)
cv.waitKey(0)
cv.destroyAllWindows()
