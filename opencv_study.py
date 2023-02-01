import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# # 读取图像
# img = cv.imread('messi5.jpg', 0)
# # 显示图像
# cv.imshow('image', img)
#
# # 如果使用的是64位计算机，则必须 k = cv.waitKey(0) 按如下所示修改行： k = cv.waitKey(0) & 0xFF
# k = cv.waitKey(0) & 0xFF
# if k == 27:  # 等待ESC退出
#     cv.destroyAllWindows()
# elif k == ord('s'):  # 等待关键字，保存和退出
#     # 写入图像
#     cv.imwrite('messigray.png', img)
#     cv.destroyAllWindows()
#
# # 使用Matplotlib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])  # 隐藏 x 轴和 y 轴上的刻度值
# plt.show()


# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     # 逐帧捕获
#     ret, frame = cap.read()
#     print(
#         cap.get(cv.CAP_PROP_FRAME_WIDTH),
#         cap.get(cv.CAP_PROP_FRAME_HEIGHT)
#     )
#     # 如果正确读取帧，ret为True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # 我们在框架上的操作到这里
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # 显示结果帧e
#     cv.imshow('frame', gray)
#     if cv.waitKey(1) == ord('q'):
#         break
# # 完成所有操作后，释放捕获器
# cap.release()
# cv.destroyAllWindows()


# cap = cv.VideoCapture('vtest.avi')
# while cap.isOpened():
#     ret, frame = cap.read()
#     # 如果正确读取帧，ret为True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     cv.imshow('frame', gray)
#     if cv.waitKey(1) == ord('q'):
#         break
# cap.release()
# cv.destroyAllWindows()
#
# cap = cv.VideoCapture(0)
# # 定义编解码器并创建VideoWriter对象
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
# print(out)
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     frame = cv.flip(frame, 0)
#     # 写翻转的框架
#     out.write(frame)
#     cv.imshow('frame', frame)
#     if cv.waitKey(1) == ord('q'):
#         break
# # 完成工作后释放所有内容
# cap.release()
# out.release()
# cv.destroyAllWindows()

# 创建黑色的图像
img = np.zeros((512, 512, 3), np.uint8)
# 绘制一条厚度为5的蓝色对角线
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
cv.imshow('tupm', img)
k = cv.waitKey(0) & 0xFF
if k == 27:  # 等待ESC退出
    cv.destroyAllWindows()
elif k == ord('s'):  # 等待关键字，保存和退出
    # 写入图像
    cv.imwrite('tupm.png', img)
    cv.destroyAllWindows()
