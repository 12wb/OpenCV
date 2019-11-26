import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('test.png')
imggray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# plt.imshow(imggray,cmap=plt.cm.gray)
hist = cv.calcHist([img],[0],None,[256],[0,255])
plt.figure()
plt.title('grayhist')
plt.xlabel('bins')
plt.ylabel('fixels')
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

