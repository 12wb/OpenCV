# import cv2 as cv
# img = cv.imread('y.jpg',0)
# cv.imshow('img',img)
#
# def nothing(x):
#     pass
#
# cv.namedWindow('Canny')
# cv.createTrackbar('threshold1','Canny',0,255,nothing)
# cv.createTrackbar('threshold2','Canny',0,255,nothing)
#
# while True:
#     threshold1 = cv.getTrackbarPos('threshold1','Canny')
#     threshold2 = cv.getTrackbarPos('threshold2','Canny')
#     edges = cv.Canny(img,threshold1,threshold2)
#     cv.imshow('Canny',edges)
#     k = cv.waitKey(25) & 0XFF
#     if chr(k) == 'q':
#         break
# cv.destroyAllWindows()

import cv2 as cv
img = cv.imread('./spdst.jpg')

def nothing(x):
    pass

cv.namedWindow("bizhigang")
cv.createTrackbar("thresh1","bizhigang",0,255,nothing)
cv.createTrackbar("thresh2","bizhigang",0,255,nothing)

while True:
    thresh1 = cv.getTrackbarPos("thresh1","bizhigang")
    thresh2 = cv.getTrackbarPos("thresh2","bizhigang")
    cv.Canny(img,thresh1,thresh2)
    edge = cv.Canny(img,thresh1,thresh2)
    cv.imshow("bizhigang",edge)

    k = cv.waitKey(25) & 0XFF
    if chr(k) == 'q':
        break
cv.destroyAllWindows()