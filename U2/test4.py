import cv2 as cv
img_path = './test.png'
imgbar1 = cv.imread(img_path, 0)
cv.imwrite('test.jpg',imgbar1) # 可以修改文件格式，并且保存
