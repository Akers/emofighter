# -*- coding:utf-8 -*-
#__author__ = 'akers'

from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import cv2
import numpy

CONST_IMG_WIDTH = 250
CONST_IMG_HEIGH = 250


def draw_emo(bg, face, txt):
    """绘制表情图，利用opencv，智能识别表情插入位置
    Args:
        bg: 底图
        face: 前脸
        txt: 文本

    Returns:
        Image

    Raises:
    """
    bg_img = cv2.imread(bg)
    f_img = cv2.imread(face)
    # 读入背景的灰度图，方便进行处理
    bg_img_gray = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
    
    #Otsu 滤波，产生二值化的图片
    ret2,th_bg = cv2.threshold(bg_img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #第一步，找出图片中的熊猫轮廓
    # 将熊猫弄成白色
    th_bg_inv = cv2.bitwise_not(th_bg)
    # 找轮廓
    image,cnts,hierarchy = cv2.findContours(th_bg_inv,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    areas_s_idx = contours_sort_idx(cnts)
    bg_mask = th_bg_inv.copy()
    # 将熊猫区域内填充黑色，形成mask
    cv2.drawContours(bg_mask, cnts, areas_s_idx[0], (255,255,255), cv2.FILLED)
    # bg_mask = cv2.bitwise_not(bg_mask)
    # 使用下面的方式进行抠图，把原图与一个黑色的图片叠加，mask为蒙版，蒙版中白色的地方会进行add，黑色区域的像素会被删除（变成黑色）
    face_bg_cntimg=cv2.add(th_bg, th_bg, mask=bg_mask)
    # 产生的face_cntimg中，只有表情所在的轮廓是白的，其他都是黑的，可能存在噪点，通过面积排序去除干扰
    image,face_bg_cnts,hierarchy = cv2.findContours(face_bg_cntimg,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    image = bg_img.copy()
    areas_s_idx = contours_sort_idx(face_bg_cnts)
    rect = cv2.minAreaRect(face_bg_cnts[areas_s_idx[0][0]])
    box = cv2.boxPoints(rect)
    # 将box缩小一下，让图片插入的位置更好看
    # cv2.drawContours(image,[numpy.int0(box)],0,(255,0,0),2)
    # cv2.imshow("image", image)
    offset = 20
    box[0][0] = box[0][0] + offset
    box[0][1] = box[0][1] - offset
    box[1][0] = box[1][0] + offset
    box[1][1] = box[1][1] + offset
    box[2][0] = box[2][0] - offset
    box[2][1] = box[2][1] + offset
    box[3][0] = box[3][0] - offset
    box[3][1] = box[3][1] - offset
    roi = bg_img[int(box[1][1]):int(box[0][1]), int(box[0][0]):int(box[2][0])]
    f_img_resize = cv2.resize(f_img, roi.shape[-2::-1])
    
    # cv2.drawContours(image,[numpy.int0(box)],0,(0,0,255),2)
    # cv2.imshow("image", image)
    # cv2.waitKey()
    # 单纯的add对这种黑白图片，效果很糟糕
    # roi = cv2.add(roi, f_img_resize)
    # 读入表情的灰度图，方便进行处理
    fg_img_gray = cv2.cvtColor(f_img_resize, cv2.COLOR_BGR2GRAY)
    
    #Otsu 滤波，产生二值化的图片
    ret2,mask = cv2.threshold(fg_img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    mask_inv = cv2.bitwise_not(mask)
    # 背景图，去掉表情中的黑色部分的像素
    img1_bg = cv2.bitwise_and(roi, roi, mask = mask)
    # 表情图，去掉图片中的白色部分
    img2_fg = cv2.bitwise_and(f_img_resize, f_img_resize, mask = mask_inv)
    dst = cv2.add(img1_bg, img2_fg)
    bg_img[int(box[1][1]):int(box[0][1]), int(box[0][0]):int(box[2][0])] = dst
    image_result = Image.fromarray(cv2.cvtColor(bg_img,cv2.COLOR_BGR2RGB))
    # 创建底图
    target = Image.new(
        'RGBA', (CONST_IMG_WIDTH, CONST_IMG_HEIGH), (255, 255, 255, 255))
    # 表情背景贴到底图上
    target.paste(image_result, (0, 0))
    # 计算文本插入y坐标
    target = draw_text(txt, target, off_set=(5, bg_img.shape[0]), allign='center')
    return target

def contours_sort_idx(contours):
    """轮廓排序
    """
    # 按面积排序
    areas = numpy.zeros(len(contours))
    for idx,cont in enumerate(contours): 
        areas[idx] = cv2.contourArea(cont)

    return cv2.sortIdx(areas, cv2.SORT_DESCENDING | cv2.SORT_EVERY_COLUMN)

def draw_text(text, image, off_set=(0, 200), allign='center'):
    """强化版绘制文字v4，默认使用30号的雅黑字体，
        并尝试适应横向空间以及居中显示
        如果文本过长自适应减少字号
    Args:
        text: 显示在图片上的文本
        image: 当前正使用的Image
        off_set: 偏移量，用于保留最小编剧，(x, y)以像素未单位
        allign: 排版，left左对齐，center居中，right右对齐

    Returns:
        Image

    Raises:

    """
    # 加入文字
    # ImageDraw为PIL的绘图模块
    _DEFAULT_FONT_SIZE = 30
    draw = ImageDraw.Draw(image)
    imageFont = ImageFont.truetype('./resources/msyh.ttc', _DEFAULT_FONT_SIZE)
    _MAX_TXT_HEIGH = 32
    txtSize = draw.textsize(text, imageFont)

    # 处理过长的文本
    textLen = txtSize[0]
    fontSize = _DEFAULT_FONT_SIZE
    # 方法2：通过简单的数据分析，我们研究出字体宽度 = 字体字号这一函数
    def char_len(text_size):
        return text_size
    # 减小字号，直到 字数*单位宽度 适应空白区域宽度
    while char_len(fontSize) * len(text) > (CONST_IMG_WIDTH - 2*off_set[0]):
        fontSize -= 1

    textLen = fontSize * len(text)

    imageFont = ImageFont.truetype('./resources/msyh.ttc', fontSize)
    realTxtSize = draw.textsize(text, imageFont)


    # 计算x坐标
    pos_x = {
        # 居中对齐
        'center': lambda max_width, txt_len, off: (max_width / 2 - txt_len / 2 if max_width > txt_len else 0) + off,
        # 左对齐
        'left': lambda max_width, txt_len, off: (off if max_width > txt_len else 0),
        # 右对齐
        'right': lambda max_width, txt_len, off: (max_width - txt_len if max_width > txt_len else 0)
    }[allign if allign in ('center', 'left', 'right') else 'center'](CONST_IMG_WIDTH - 2*off_set[0], realTxtSize[0], off_set[0])

    print("当前X坐标", pos_x, ", max_width:", CONST_IMG_WIDTH - 2*off_set[0], ",text_len: ", realTxtSize[0])
    # 默认显示位置
    pos = (pos_x, off_set[1])

    # 底图上的10,200位置写入文字
    draw.text(pos, text, fill='black', font=imageFont)
    del draw
    return image
