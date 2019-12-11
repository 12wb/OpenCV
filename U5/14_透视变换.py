import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('./sudoku.jpg')
row,cols,ch = img.shape
# print(row,cols,ch)

pts1 = np.float32([[56,65],[368,52],[28,387],[390,39]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("input")
plt.subplot(1,2,2)
plt.imshow(dst)
plt.title("output")
plt.show()

