# import cv2
# import os
# import numpy as np
#
#
# # 检测人脸
# def detect_face(img):
#     # 将测试图像转换为灰度图像，因为opencv人脸检测器需要灰度图像
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # 加载OpenCV人脸检测分类器Haar
#     face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
#
#     # 检测多尺度图像，返回值是一张脸部区域信息的列表（x,y,宽,高）
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
#
#     # 如果未检测到面部，则返回原始图像
#     if (len(faces) == 0):
#         return None, None
#
#     # 目前假设只有一张脸，xy为左上角坐标，wh为矩形的宽高
#     (x, y, w, h) = faces[0]
#
#     # 返回图像的正面部分
#     return gray[y:y + w, x:x + h], faces[0]
#
#
# # 该函数将读取所有的训练图像，从每个图像检测人脸并将返回两个相同大小的列表，分别为脸部信息和标签
# def prepare_training_data(data_folder_path):
#     # 获取数据文件夹中的目录（每个主题的一个目录）
#     dirs = os.listdir(data_folder_path)
#
#     # 两个列表分别保存所有的脸部和标签
#     faces = []
#     labels = []
#
#     # 浏览每个目录并访问其中的图像
#     for dir_name in dirs:
#         # dir_name(str类型)即标签
#         label = int(dir_name)
#         # 建立包含当前主题主题图像的目录路径
#         subject_dir_path = data_folder_path + "/" + dir_name
#         # 获取给定主题目录内的图像名称
#         subject_images_names = os.listdir(subject_dir_path)
#
#         # 浏览每张图片并检测脸部，然后将脸部信息添加到脸部列表faces[]
#         for image_name in subject_images_names:
#             # 建立图像路径
#             image_path = subject_dir_path + "/" + image_name
#             # 读取图像
#             image = cv2.imread(image_path)
#             # 显示图像0.1s
#             cv2.imshow("Training on image...", image)
#             cv2.waitKey(100)
#
#             # 检测脸部
#             face, rect = detect_face(image)
#             # 我们忽略未检测到的脸部
#             if face is not None:
#                 # 将脸添加到脸部列表并添加相应的标签
#                 faces.append(face)
#                 labels.append(label)
#
#     cv2.waitKey(1)
#     cv2.destroyAllWindows()
#     # 最终返回值为人脸和标签列表
#     return faces, labels
#
#
# # 调用prepare_training_data（）函数
# faces, labels = prepare_training_data("training_data")
#
# # 创建LBPH识别器并开始训练，当然也可以选择Eigen或者Fisher识别器
# face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.train(faces, np.array(labels))
#
#
# # 根据给定的（x，y）坐标和宽度高度在图像上绘制矩形
# def draw_rectangle(img, rect):
#     (x, y, w, h) = rect
#     cv2.rectangle(img, (x, y), (x + w, y + h), (128, 128, 0), 2)
#
#
# # 根据给定的（x，y）坐标标识出人名
# def draw_text(img, text, x, y):
#     cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (128, 128, 0), 2)
#
#
# # 建立标签与人名的映射列表（标签只能为整数）
# subjects = ["jiaju", "jiaqiang"]
#
#
# # 此函数识别传递的图像中的人物并在检测到的脸部周围绘制一个矩形及其名称
# def predict(test_img):
#     # 生成图像的副本，这样就能保留原始图像
#     img = test_img.copy()
#     # 检测人脸
#     face, rect = detect_face(img)
#     # 预测人脸
#     label = face_recognizer.predict(face)
#     # 获取由人脸识别器返回的相应标签的名称
#     label_text = subjects[label[0]]
#
#     # 在检测到的脸部周围画一个矩形
#     draw_rectangle(img, rect)
#     # 标出预测的名字
#     draw_text(img, label_text, rect[0], rect[1] - 5)
#     # 返回预测的图像
#     return img
#
#
# # 加载测试图像
# test_img1 = cv2.imread("test_data/test1.jpg")
# test_img2 = cv2.imread("test_data/test2.jpg")
#
# # 执行预测
# predicted_img1 = predict(test_img1)
# predicted_img2 = predict(test_img2)
#
# # 显示两个图像
# cv2.imshow(subjects[0], predicted_img1)
# cv2.imshow(subjects[1], predicted_img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Path to image or video. Skip to capture frames from camera')
parser.add_argument('--thr', default=0.2, type=float, help='Threshold value for pose parts heat map')
parser.add_argument('--width', default=368, type=int, help='Resize input to specific width.')
parser.add_argument('--height', default=368, type=int, help='Resize input to specific height.')

args = parser.parse_args()

BODY_PARTS = {"Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
              "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
              "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
              "LEye": 15, "REar": 16, "LEar": 17, "Background": 18}

POSE_PAIRS = [["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
              ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
              ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
              ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
              ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"]]

inWidth = args.width
inHeight = args.height

net = cv.dnn.readNetFromTensorflow("graph_opt.pb")

cap = cv.VideoCapture(args.input if args.input else 0)

while cv.waitKey(1) < 0:
    hasFrame, frame = cap.read()
    if not hasFrame:
        cv.waitKey()
        break

    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]

    net.setInput(cv.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight), (127.5, 127.5, 127.5), swapRB=True, crop=False))
    out = net.forward()
    out = out[:, :19, :, :]  # MobileNet output [1, 57, -1, -1], we only need the first 19 elements

    assert (len(BODY_PARTS) == out.shape[1])

    points = []
    for i in range(len(BODY_PARTS)):
        # Slice heatmap of corresponging body's part.
        heatMap = out[0, i, :, :]

        # Originally, we try to find all the local maximums. To simplify a sample
        # we just find a global one. However only a single pose at the same time
        # could be detected this way.
        _, conf, _, point = cv.minMaxLoc(heatMap)
        x = (frameWidth * point[0]) / out.shape[3]
        y = (frameHeight * point[1]) / out.shape[2]
        # Add a point if it's confidence is higher than threshold.
        points.append((int(x), int(y)) if conf > args.thr else None)

    for pair in POSE_PAIRS:
        partFrom = pair[0]
        partTo = pair[1]
        assert (partFrom in BODY_PARTS)
        assert (partTo in BODY_PARTS)

        idFrom = BODY_PARTS[partFrom]
        idTo = BODY_PARTS[partTo]

        if points[idFrom] and points[idTo]:
            cv.line(frame, points[idFrom], points[idTo], (0, 255, 0), 3)
            cv.ellipse(frame, points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)
            cv.ellipse(frame, points[idTo], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)

    t, _ = net.getPerfProfile()
    freq = cv.getTickFrequency() / 1000
    cv.putText(frame, '%.2fms' % (t / freq), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    cv.imshow('OpenPose using OpenCV', frame)

