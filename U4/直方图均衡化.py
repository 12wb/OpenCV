import numpy as np
import cv2 as cv

def calcdrawhist(img,color):
    hist = cv.calcHist([img],[0],None,[256],[0.0,255.0])
    minVal,maxVal,minLoc,maxLoc = cv.minMaxLoc(hist)  # 统计最大值，最小值
    histimg = np.zeros([256,256,3],np.uint8) # 黑色
    hpt = int(0.9*256)  # 直方图在0.9到255之间
    for h in range(256):
        intensity = int(hist[h]*hpt/maxVal)  # 密度
        cv.line(histimg,(h,256),(h,256-intensity),color)
    return histimg

def main():
    test = cv.imread('./forCLA.png')
    gray = cv.cvtColor(test,cv.COLOR_BGR2GRAY)
    equ = cv.equalizeHist(gray)  # 均衡化
    cla = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))  # 自适应
    cll = cla.apply(gray)
    cv.imshow('imshow',np.hstack((gray,equ,cll)))
    hist_gray = calcdrawhist(gray,(255,255,255))
    hist_equ = calcdrawhist(equ,(255,255,255))
    hist_cll = calcdrawhist(cll,(255,255,255))
    cv.imshow('histshow',np.hstack((hist_gray,hist_equ,hist_cll)))
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__=='__main__':
    main()
