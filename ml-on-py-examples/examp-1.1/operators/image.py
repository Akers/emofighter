# -*- coding:utf-8 -*-
#__author__ = 'akers'

from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

CONST_IMG_WIDTH = 250
CONST_IMG_HEIGH = 250

def draw_emo(bg, face, txt):
    """绘制表情图
    Args:
        bg: 底图
        face: 前脸
        txt: 文本

    Returns:
        Image

    Raises:

    """
    # 创建底图
    target = Image.new(
        'RGBA', (CONST_IMG_WIDTH, CONST_IMG_HEIGH), (255, 255, 255, 255))
    # 导入表情背景
    background = Image.open(bg)
    # 表情背景贴到底图上
    target.paste(background, (0, 0))
    # 导入表情
    faceImg = Image.open(face)
    target.paste(faceImg, (62, 37))

    # 加入文本
    # target = draw_text(txt, target)
    # target = draw_text_v1(txt, target, off_set=200)
    target = draw_text_v2(txt, target, off_set=(10, 200), allign='center')
    return target

def draw_text(text, image):
    """绘制文字，默认使用30号的雅黑字体，并尝试适应横向空间以及居中显示
    Args:
        text: 显示在图片上的文本
        image: 当前正使用的Image

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

    # 底图上的10,200位置写入文字
    draw.text((10, 200), text, fill='black', font=imageFont)
    del draw
    return image

def draw_text_v1(text, image, off_set=200):
    """强化版绘制文字v1，让文字在x轴上居中
    Args:
        text: 显示在图片上的文本
        image: 当前正使用的Image
        off_set: 纵向偏移量

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
    pos_x = (CONST_IMG_WIDTH - txtSize[0]) / 2 if CONST_IMG_WIDTH > txtSize[0] else 0
    print("当前X坐标", pos_x)
    # 默认显示位置
    pos = (pos_x, off_set)
    draw.text(pos, text, fill='black', font=imageFont)
    del draw
    return image

def draw_text_v2(text, image, off_set=(0, 200), allign='center'):
    """强化版绘制文字v2，左中右，想放哪里放哪里
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
    imageFont = ImageFont.truetype('./resources/msyh.ttc', 30)

    # 计算x坐标
    pos_x = {
        # 居中对齐
        'center': lambda max_width, txt_len, off: (max_width / 2 - txt_len / 2 if max_width > txt_len else 0) + off,
        # 左对齐
        'left': lambda max_width, txt_len, off: (off if max_width > txt_len else 0),
        # 右对齐
        'right': lambda max_width, txt_len, off: (max_width - txt_len if max_width > txt_len else 0)
    }[allign if allign in ('center', 'left', 'right') else 'center'](CONST_IMG_WIDTH - 2*off_set[0], txtSize[0], off_set[0])

    # 实际上是这样
    def center(max_width, txt_len, off):
        return (max_width / 2 - txt_len / 2 if max_width > txt_len else 0) + off

    def left(max_width, txt_len, off):
        return off if max_width > txt_len else 0

    def right(max_width, txt_len, off):
        return max_width - txt_len if max_width > txt_len else 0
    
    dict_temp = {
        # 居中对齐
        'center': center,
        # 左对齐
        'left': left,
        # 右对齐
        'right': right
    }

    pos_x_func = dict_temp[allign if allign in ('center', 'left', 'right') else 'center']
    pos_x = pos_x_func(CONST_IMG_WIDTH - 2*off_set[0], txtSize[0], off_set[0])

    # 转换成if-else之后：
    # max_width = CONST_IMG_WIDTH - 2*off_set[0]
    # txt_len = txtSize[0]
    # if allign == 'center':
    #     pos_x = (max_width / 2 - txt_len / 2 if max_width > txt_len else 0) + off_set[0]
    # else if allign == 'left':
    #     pos_x = off_set[0] if CONST_IMG_WIDTH - 2*off_set[0] > txt_len else 0
    # else if allign == 'right':
    #     pos_x = max_width - txt_len if max_width > txt_len else 0
    # else:
    #     pos_x = ((max_width / 2 - txt_len / 2 if max_width > txt_len else 0) + off_set[0]



    # 默认显示位置
    pos = (pos_x, off_set[1])

    # 底图上的10,200位置写入文字
    draw.text(pos, text, fill='black', font=imageFont)
    del draw
    return image