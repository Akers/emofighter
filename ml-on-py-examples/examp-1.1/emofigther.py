# -*- coding:utf-8 -*-
#__author__ = 'akers'
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import win32clipboard as clip
import sys
import platform
import win32con
import matplotlib.pyplot as plt

CONST_IMG_WIDTH = 250
CONST_IMG_HEIGH = 250


def main(argv):

    # 创建底图
    target = Image.new(
        'RGBA', (CONST_IMG_WIDTH, CONST_IMG_HEIGH), (255, 255, 255, 255))
    # 导入表情背景
    background = Image.open('./resources/background/pander/default.png')
    # 表情背景贴到底图上
    target.paste(background, (0, 0))
    # 导入表情
    faceImg = Image.open('./resources/face/jgz/laugth.png')
    target.paste(faceImg, (62, 37))

    # 加入文本
    target = draw_text(argv[1], target, off_set=(5, 200), allign='center')

    # 保存图片
    # 如果是win32系统，可以直接怼到剪切板里
    if 'Windows' in platform.platform() or 'windows' in platform.platform():
        output = BytesIO()
        clip.OpenClipboard()  # 打开剪贴板
        clip.EmptyClipboard()  # 先清空剪贴板
        target.save(output, format="BMP")
        data = output.getvalue()[14:]
        clip.SetClipboardData(win32con.CF_DIB, data)  # 将图片放入剪贴板
        clip.CloseClipboard()
        output.close()
    else:
        target.save('output/facing.png')

    # 调试用
    # plt.figure("生成表情包")
    # plt.imshow(target)
    # plt.show()


def draw_text(text, image, off_set=(0, 200), allign='center'):
    """绘制文字，默认使用30号的雅黑字体，并尝试适应横向空间以及居中显示
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
    DEFAULT_FONT_SIZE = 30
    draw = ImageDraw.Draw(image)
    imageFont = ImageFont.truetype('./resources/msyh.ttc', DEFAULT_FONT_SIZE)
    MAX_TXT_HEIGH = 35
    txtSize = draw.textsize(text, imageFont)

    # 处理过长的文本
    textLen = txtSize[0]
    fontSize = DEFAULT_FONT_SIZE
    # 方法1：笨方法，不断减小字号，直到塞得下
    while (CONST_IMG_WIDTH <= textLen + 2*off_set[0]) and fontSize >= 10:
        fontSize -= 1
        imageFont = ImageFont.truetype('./resources/msyh.ttc', fontSize)
        textLen = draw.textsize(text, imageFont)[0]
        print("当前字号{}，文本宽度{}".format(fontSize, textLen))
    # 问题1：如果减小到最小字号，仍然塞不下呢？如何处理换行问题？多少长度下需要换行？
    # 问题2：是否有更优雅的方法呢？
    # 方法2：针对上面两个问题，再使用方法1这种简单粗暴的方式已经难以满足
    # 根据使用的字体，计算出单个字符的宽度，然后对文本所占的面积进行预估呢

    # 计算x坐标
    pos_x = {
        # 居中对齐
        'center': lambda max_width, txt_len, off: (max_width / 2 - txt_len / 2 if max_width > txt_len else 0) + off,
        # 左对齐
        'left': lambda max_width, txt_len, off: (off if max_width > txt_len else 0),
        # 右对齐
        'right': lambda max_width, txt_len, off: (max_width - txt_len if max_width > txt_len else 0)
    }[allign if allign in ('center', 'left', 'right') else 'center'](CONST_IMG_WIDTH - 2*off_set[0], textLen, off_set[0])

    print("当前X坐标{}, max_width:{}".format(pos_x, CONST_IMG_WIDTH))
    # 默认显示位置
    pos = (pos_x, off_set[1])

    # 底图上的10,200位置写入文字
    draw.text(pos, text, fill='black', font=imageFont)
    del draw
    return image


if __name__ == "__main__":
    main(sys.argv)
