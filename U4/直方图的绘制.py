import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def main():
    test = cv.imread('./img2.jpg')
    b,g,r = cv.split(test)
    histB,bins=np.histogram(b.ravel(),256,[0,256])  # reval 归一化,256个数据,[0,256]边界

    histG = np.bincount(g.ravel(),minlength=256)
    histR = np.bincount(r.ravel(),minlength=256)
    fig,(ax1,ax2,ax3)= plt.subplots (1,3)

    ax1.plot(histB,color='b')
    ax1.set_title('B')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax2.plot(histG,color='g')
    ax2.set_title('G')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax3.plot(histR,color='r')
    ax3.set_title('R')
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    plt.show()
if __name__=='__main__':
    main()
