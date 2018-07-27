# -*- coding:utf-8 -*-
#__author__ = 'akers'
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import numpy as np
import win32clipboard as clip
import sys
import platform
import win32con
import matplotlib.pyplot as plt
from pylab import mpl
from scipy.optimize import leastsq

CONST_IMG_WIDTH = 250
CONST_IMG_HEIGH = 250


def main(argv):
    mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    """测试一个字体的大小"""
    target = Image.new(
        'RGBA', (CONST_IMG_WIDTH, CONST_IMG_HEIGH), (255, 255, 255, 255))
    draw = ImageDraw.Draw(target)
    xd = []
    yd = []
    # 准备分析数据
    for i in range(1, 31):
        imageFont = ImageFont.truetype('./resources/msyh.ttc', i)
        txtSize = draw.textsize("字", font=imageFont)
        yd.append(txtSize)
        xd.append(i)
        print("字号{}，大小{}".format(i, txtSize))
    fontWidthAnalysis(yd, xd)

    plt.ylabel(u'字体大小')
    plt.xlabel(u'字号')
    plt.legend()
    plt.show()

# 分析字体大小与宽度的关系
# yd中的数据为每个字号对应的字体大小：(width, heigh)
# xd中的数据为每个字号
def fontWidthAnalysis(yd, xd):
    fontWidthData = []
    fontHeightData = []
    for p in yd:
        fontWidthData.append(p[0])
        fontHeightData.append(p[1])
    #将数据转换成numpy数组，方便后续的操作
    Y = np.array(fontWidthData)
    X = np.array(xd)

    # 使用最小二乘拟合绘制对散点进行函数拟合
    # 定义函数形状，哈哈哈，就是 y = kx+b 直线！
    # 那问题就来了，如果我不知道该贴合哪个曲线呢？
    def func(p,x):
        k,b = p
        return k*x + b

    # 使用leastsq进行拟合，第一个参数为误差函数
    r = leastsq(lambda p,x,y: func(p,x) - y, [1, 0], args=(X, Y))
    # 计算结果中的r[0]为一个元组，为求得的k和b
    k, b = r[0]
    # 最后我们得出结论，拟合结果为y = x
    print("k=",k,"b=",b, "r=", r)

    # 画出数据点
    plt.plot(fontWidthData, xd, 'bo', label=u"字体宽度")

    # 画出拟合线
    plt.plot(X,k*X+b,color="orange",label=u"字体宽度拟合",linewidth=2) 
    
    # 分析字体高度
    



if __name__ == "__main__":
    main(sys.argv)
