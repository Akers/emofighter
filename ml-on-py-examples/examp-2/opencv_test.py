# -*- coding:utf-8 -*-
#__author__ = 'akers'
# 测试OpenCv图像处理
import argparse
import imutils
import cv2
import numpy
import random
import PIL

import operators.image
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to the input image")
args = vars(ap.parse_args())
 
# load the image, convert it to grayscale, blur it slightly,
# and threshold it
image = cv2.imread(args["image"])
# 去色，转换成灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow("gray", gray)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 使用findContours进行轮廓查找
# mode:
#   RETR_EXTERNAL retrieves only the extreme outer contours. It sets hierarchy[i][2]=hierarchy[i][3]=-1 for all the contours.
#   RETR_LIST retrieves all of the contours without establishing any hierarchical relationships.
#   RETR_CCOMP retrieves all of the contours and organizes them into a two-level hierarchy. At the top level, there are external boundaries of the components. At the second level, there are boundaries of the holes. If there is another contour inside a hole of a connected component, it is still put at the top level.
#   RETR_TREE retrieves all of the contours and reconstructs a full hierarchy of nested contours. This full hierarchy is built and shown in the OpenCV contours.c demo.
# method:
#   CV_CHAIN_APPROX_NONE stores absolutely all the contour points. That is, any 2 subsequent points (x1,y1) and (x2,y2) of the contour will be either horizontal, vertical or diagonal neighbors, that is, max(abs(x1-x2),abs(y2-y1))==1.
#   CV_CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments and leaves only their end points. For example, an up-right rectangular contour is encoded with 4 points.
#   CV_CHAIN_APPROX_TC89_L1,CV_CHAIN_APPROX_TC89_KCOS applies one of the flavors of the Teh-Chin chain approximation algorithm. See [TehChin89] for details.
# cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# findContours返回一个元组，其第二个成员为轮廓列表
# cnts = cnts[0] if imutils.is_cv2() else cnts[1]

# 画出每条轮廓线
# 轮廓线颜色库，色彩模式是BGR...
# for i,c in enumerate(cnts):
#     cv2.drawContours(image, [c], -1, (0, 255, 0), 1)
#     cv2.imshow("Image", image)
#     cv2.waitKey(0)
# 上面的分析得出一个结论他检测到的轮廓都是图像的大白边，那怎么办呢
# 分成两步
# 1. 把熊猫抠下来
# 2. 对抠下来的熊猫进行轮廓查找

# 为了抠出整个熊猫，先把图片反色：
def inverse_color(image):

    height,width = image.shape
    img2 = image.copy()

    for i in range(height):
        for j in range(width):
            img2[i,j] = (255-image[i,j]) 
    return img2

inverse_gray = inverse_color(gray)
# cv2.imshow("Image", inverse_gray)
# cv2.waitKey(0)

#然后再试试查找轮廓
# cnts = cv2.findContours(inverse_gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if imutils.is_cv2() else cnts[1]
# for c in cnts:
#     cv2.drawContours(image, [c], -1, (0, 255, 0), 1)
#     cv2.imshow("Image", image)
#     cv2.waitKey(0)
# 这样是大致可以选中轮廓了，但还是不能完美的抠出熊猫底图的轮廓
# 要对图片进行处理，让白的更白，黑的更黑
# 高斯模糊
# blurred = cv2.GaussianBlur(gray, (1, 1), 0)
# cv2.imshow("Image blurred", blurred)
# cv2.waitKey(0)
# 二值化
thresh = cv2.threshold(inverse_gray, 0, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
# cv2.imshow("Image thresh", thresh)
# cv2.waitKey(0)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
temp_img = image.copy()
for c in cnts:
    cv2.drawContours(temp_img, [c], -1, (0, 0, 255), 3)
    # cv2.imshow("Image", temp_img)
    # cv2.waitKey(0)
# 完美的轮廓！
# drawContours还有另外一种填充模式可以把轮廓里面上色，例如我们上一个黑色
for c in cnts:
    cv2.drawContours(temp_img, [c], -1, (0, 0, 0), cv2.FILLED)
    # cv2.imshow("Image filled", temp_img)
    # cv2.waitKey(0)

# 如何再原图上把熊猫抠出来
# 先制作一个熊猫背景的模板，通过再原图上对轮廓进行填充获得形状模板
mask = gray.copy()
for c in cnts:
    cv2.drawContours(mask, [c], -1, (0, 0, 0), cv2.FILLED)
    # cv2.imshow("Image mask", mask)
    # cv2.waitKey(0)

# 将轮廓外的像素涂黑，可以采用图像逻辑运算
# 这里采用异或运算，简单来说就是对图像上每个像素进行异或
# 异或运算：1 xor 1 = 0, 1 xor 0 = 1, 0 xor 0 = 0
gray_thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
temp_img = cv2.bitwise_xor(mask, gray_thresh)
# cv2.imshow("Image bitwise_and", temp_img)
# cv2.waitKey(0)
# 然后我们再做一次轮廓查找
cnts = cv2.findContours(temp_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
image_contours2 = image.copy()
for c in cnts:
    cv2.drawContours(image_contours2, [c], -1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 3)

# cv2.imshow("image_contours2", image_contours2)

# 看每次的轮廓线，已经可以初步的发现回有包括正中空白区域的轮廓了，只要把它筛选出来就ok
# 尝试按照轮廓大小进行筛选
areas = list()
for i, cnt in enumerate(cnts):
    #cv2.contourArea 计算轮廓的面积大小
    areas.append((i, cv2.contourArea(cnt)))
#按面积大小，从大到小排序
areas = sorted(areas, key=lambda d: d[1], reverse=True)
print(areas)
image_contours_sorted = image.copy()
# cv2.imshow("image_contours_sorted", image_contours_sorted)
for i, are in areas:
    if are < 150:
        continue
    cv2.drawContours(image_contours_sorted, cnts, i, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 3)
    # cv2.imshow("image_contours_sorted", image_contours_sorted)
    # cv2.waitKey(0)

# 然后就可以把最大的轮廓找到囖：
image_contours_max = image.copy()
cv2.drawContours(image_contours_max, cnts, areas[0][0], (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 3)
# cv2.imshow("image_contours_max", image_contours_max)
# cv2.waitKey(0)

# 然后，就来确认我们表情图插入的位置了
# opencv提供了一个查找最小外接矩形的函数
# 函数返回的是一个矩形的描述，返回值示例如下：
# (中心点(x,y), 宽高(w,h), 旋转角度)
# 如((78.0, 67.5), (124.0, 115.0), -0.0) 则表示一个中心在78.0, 67.5上，宽124高115，旋转角度为0的矩形
rect = cv2.minAreaRect(cnts[areas[0][0]])
print("minAreaRect:", rect)
# 画出这个矩形
# 通过boxPoints计算出四角坐标，opencv太好了，连换算都省了
box = cv2.boxPoints(rect)
print("minAreaRect box:", box)
#画出来看看
color = (100, 255, 100)
# cv2.waitKey(0)
image_min_react = image.copy()
cv2.line(image_min_react, (box[0][0], box[0][1]), (box[1][0], box[1][1]), color, 3)
cv2.line(image_min_react, (box[1][0], box[1][1]), (box[2][0], box[2][1]), color, 3)
cv2.line(image_min_react, (box[2][0], box[2][1]), (box[3][0], box[3][1]), color, 3)
cv2.line(image_min_react, (box[3][0], box[3][1]), (box[0][0], box[0][1]), color, 3)
# cv2.imshow("image_min_react", image_min_react)
# cv2.waitKey(0)

# 整理一下，我们现在有以下的数据了：
# 1. 头像区域的轮廓：
face_area_cnt = cnts[areas[0][0]]
# 2. 头像区域的最小贴合矩形
rect = cv2.minAreaRect(cnts[areas[0][0]])
# 3. 最小贴合矩形的四角坐标
box = cv2.boxPoints(rect)

# 下一步就是把表情加进来，调整好大小位置，然后放到底图上
face = cv2.imread('D:\\Files\\Projects\\ml\\python\\emofighter\\ml-on-py-examples\\examp-2\\resources\\face\\jgz\\awkward.png')
# 调整到合适的大小
face = cv2.resize(face, (int(rect[1][0]), int(rect[1][1])))
# cv2.imshow("face: ", face)
# 选取外接矩形的面积
# 这里要注意，opencv的box模型，x坐标最小，y最大的一点为矩形的原点（），顺时针分别是第一、第二、第三顶点，原点与第三顶点连线与过原点的x轴平行线的夹角即为矩形的偏转系数
rs=int(box[1][1])
re=int(box[0][1])
cs=int(box[1][0])
ce=int(box[2][0])
print("rs:",rs,"re:",re,"cs:",cs,"ce",ce)
image_result1 = image.copy()
roi = image_result1[rs:re, cs:ce]
cv2.imshow("roi: ", roi)
cv2.waitKey(0)
dst = cv2.addWeighted(face, 1, roi, 0, 0)
# cv2.imshow("dst: ", dst)
# cv2.waitKey(0)
image_result1[rs:re, cs:ce] = dst
# cv2.imshow("result: ", image_result1)
# cv2.waitKey(0)

# 合并的并不理想，如何实现PIL那种让表情图背景透明呢？
# 通过使用遮罩(mask)来删除
# 创建掩膜
image_result2 = image.copy()
roi = image_result2[rs:re, cs:ce]
# cv2.imshow("roi2: ", roi)
face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
# cv2.imshow("mask: ", mask)
# cv2.imshow("mask: ", mask_inv)
# mask_bg = cv2.bitwise_and(roi,roi,mask=mask)
# mask_fg = cv2.add(face,face,mask=mask_inv)
# cv2.imshow("mask_bg", mask_bg)
# cv2.imshow("mask", mask)
# cv2.imshow("add: ", cv2.add(face, roi))
# cv2.imshow("add with mask: ", cv2.add(face, roi, mask=mask))
# cv2.imshow("bitwise_xor: ", cv2.bitwise_xor(face, roi))
# cv2.imshow("bitwise_xor with mask: ", cv2.bitwise_xor(face, roi, mask=mask))
# cv2.imshow("bitwise_or: ", cv2.bitwise_or(face, roi))
# cv2.imshow("bitwise_or with mask: ", cv2.bitwise_or(face, roi, mask=mask))
cv2.imshow("bitwise_and: ", cv2.bitwise_and(face, roi))
# 看来效果最好的是bitwise_and
# 为什么呢？
# 1. 我们的是二值化的图像（黑白），因此对于每个像素，会有以下几种情况（1为白，0为黑）：0&&0=0 1&&0=0 1&&1=1
# 所以达到了表情上的白色像素不会遮盖到底图的黑色像素！
# dst = cv2.add(face, mask_bg)
# cv2.imshow("result2: ", dst)mask_inv
# 但是如果表情图或背景图不是纯色呢

# 尝试1：把表情图做成模板
mask = cv2.threshold(face_gray, 0, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
mask_inv = cv2.bitwise_not(mask)
cv2.imshow("mask: ", mask)
cv2.imshow("mask_inv: ", mask_inv)
image_result3 = image.copy()
roi2 = image_result3[rs:re, cs:ce]
face.copyTo(roi2, mask=mask_inv)
cv2.imshow("roi2: ", roi2)
cv2.waitKey(0)