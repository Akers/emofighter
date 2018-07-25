# -*- coding:utf-8 -*-
#__author__ = 'akers'
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO
import win32clipboard as clip
import sys, platform, win32con
import matplotlib.pyplot as plt


def main(argv):

    #创建底图
    target=Image.new('RGBA', (250, 250), (255, 255, 255, 255))
    #导入表情背景
    background=Image.open('./resources/background/pander/default.png')
    #表情背景贴到底图上
    target.paste(background, (0,0))
    #导入表情
    faceImg=Image.open('./resources/face/jgz/laugth.png')
    target.paste(faceImg, (62,37))

    #加入文本
    target = draw_text(argv[1], target)

    #保存图片
    #如果是win32系统，可以直接怼到剪切板里
    if 'Windows' in platform.platform() or 'windows' in platform.platform():
        output = BytesIO()
        clip.OpenClipboard() #打开剪贴板
        clip.EmptyClipboard()  #先清空剪贴板
        target.save(output, format="BMP")
        data = output.getvalue()[14:]
        clip.SetClipboardData(win32con.CF_DIB, data)  #将图片放入剪贴板
        clip.CloseClipboard()
        output.close()
    else:
        target.save('output/facing.png')

    #调试用
    # plt.figure("生成表情包")
    # plt.imshow(target)
    # plt.show()

def draw_text(text, image, off_set = (10, 200), allign = 'center'):
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
    #加入文字
    #ImageDraw为PIL的绘图模块
    draw = ImageDraw.Draw(image)
    imageFont = ImageFont.truetype('./resources/msyh.ttc', 30)
    MAX_WIDTH=230
    MAX_HEIGH=35
    txtSize = draw.textsize(text, imageFont)

    #计算x坐标
    pox_x = {
    'center': lambda max_width, txt_len, off_set: (max_width / 2 - txt_len / 2 + off_set if max_width > txt_len + 2*off_set else 0),
    'left': lambda max_width, txt_len, off_set: (off_set if max_width > txt_len + 2*off_set else 0),
    'right': lambda max_width, txt_len, off_set: (max_width - txt_len - off_set if max_width > txt_len + 2*off_set else 0)
    }[allign](MAX_WIDTH, txtSize[0], off_set[0])

    #默认显示位置
    pos = (pox_x, off_set[1])
    #尝试计算字符宽度
    print(draw.textsize(text, imageFont))
    #底图上的10,200位置写入文字
    draw.text(pos, text,fill='black', font=imageFont)
    del draw
    return image

if __name__ == "__main__":
      main(sys.argv)