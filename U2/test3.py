import cv2 as cv
img_path = './test.png'
img = cv.imread(img_path,0)
cv.namedWindow('imgt1',cv.WINDOW_AUTOSIZE)
cv.namedWindow('imgt2',cv.WINDOW_NORMAL)
imgbgr1 = cv.imread(img_path,cv.IMREAD_COLOR)
imgbgr2 = cv.imread(img_path,0)
cv.imshow('imgt1',imgbgr1)
cv.imshow('imgt1',imgbgr2)
cv.waitKey(0)
cv.destroyAllWindows()

