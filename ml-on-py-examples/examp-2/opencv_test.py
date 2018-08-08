# -*- coding:utf-8 -*-
#__author__ = 'akers'
# 测试OpenCv图像处理
import argparse
import imutils
import cv2
import numpy
 
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
cv2.imshow("Image", inverse_gray)
cv2.waitKey(0)

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
cv2.imshow("Image thresh", thresh)
cv2.waitKey(0)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
temp_img = image.copy()
for c in cnts:
    cv2.drawContours(temp_img, [c], -1, (0, 255, 0), 1)
    cv2.imshow("Image", temp_img)
    cv2.waitKey(0)
# 完美的轮廓！
# drawContours还有另外一种填充模式可以把轮廓里面上色，例如我们上一个黑色
temp_img = image.copy()
for c in cnts:
    cv2.drawContours(temp_img, [c], -1, (0, 0, 0), cv2.FILLED)
    cv2.imshow("Image", temp_img)
    cv2.waitKey(0)



# cv2.imshow("Image bitwise_and", cv2.bitwise_or(temp_img, image))
# cv2.waitKey(0)