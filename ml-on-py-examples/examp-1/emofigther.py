# -*- coding:utf-8 -*-
#__author__ = 'akers'
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO
import win32clipboard as clip
import sys, platform, win32con
import matplotlib.pyplot as plt


def main(argv):

    #创建底图
    target=Image.new('RGBA', (250, 250), (0, 0, 0, 0))
    #导入表情背景
    background=Image.open('./resources/background/pander/default.png')
    #表情背景贴到底图上
    target.paste(background, (0,0))
    #导入表情
    faceImg=Image.open('./resources/face/jgz/laugth.png')
    target.paste(faceImg, (62,37))
    #加入文字
    #ImageDraw为PIL的绘图模块
    draw = ImageDraw.Draw(target)
    font = ImageFont.truetype('./resources/msyh.ttc', 30)
    #底图上的10,200位置写入文字
    draw.text((10, 200), argv[1],fill='black', font=font)
    del draw
    #如果是win32系统，可以直接怼到剪切板里
    if 'Windows' in platform.platform() or 'windows' in platform.platform():
        # 打开字节流
        output = BytesIO()
        # 打开剪贴板
        clip.OpenClipboard() 
        # 先清空剪贴板
        clip.EmptyClipboard()
        # 将图片保存到字节流
        target.save(output, format="BMP")
        # 去掉字节流中的前14个字符（BMP位图文件头）
        data = output.getvalue()[14:]
        # 将图片放入剪贴板，这里是不带文件头的数据
        clip.SetClipboardData(win32con.CF_DIB, data) 
        clip.CloseClipboard()
        output.close()
    #保存图片
    target.save('output/facing.png')
    #调试用，用pyplot可以方便的以弹出窗的形式展示可视化内容
    # plt.figure("生成表情包")
    # plt.imshow(target)
    # plt.show()
    
 
if __name__ == "__main__":
      main(sys.argv)