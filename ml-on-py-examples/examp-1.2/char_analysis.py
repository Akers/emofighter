#!/usr/bin/python3
# -*- coding:utf-8 -*-
#__author__ = 'akers'
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
from scipy.optimize import leastsq
import random


CONST_IMG_WIDTH = 250
CONST_IMG_HEIGH = 250

def main(argv):
    mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    """测试一个字体的大小"""
    target = Image.new(
        'RGBA', (CONST_IMG_WIDTH, CONST_IMG_HEIGH), (255, 255, 255, 255))
    draw = ImageDraw.Draw(target)
    # 准备分析数据
    font_num = []
    text_size = []
    for i in range(1, 500):
        imageFont = ImageFont.truetype('./resources/msyh.ttc', i)
        char_size = draw.textsize("字", font=imageFont)
        text_size.append((char_size[0] + random.randint(-10,10), char_size[1]))
        font_num.append(i)


    # scatter画出散点图，以字号为x轴，字体宽度为y轴
    # 在分析前，先绘制散点图，对大致的函数形状进行分析
    plt.scatter(list(map(lambda x: x[0], text_size)), font_num, 1, color="b", label=u"字体宽度")


    #将字体大小数据用numpy转化成一个二维数组
    _font_size_np = np.array(text_size)
    #将字号转换为numpy数组
    _font_num_np = np.array(font_num)
    Y = _font_size_np[:,0]
    X = _font_num_np

    # 使用最小二乘拟合绘制对散点进行函数拟合
    def func_shape(p, x):
        """定义函数形状，哈哈哈，就是 y = kx+b 直线！
        Args:
            p: 常数
            x: 自变量
        Returns:
            函数运算求得的因变量
        """
        k,b = p
        return k*x + b

    def func_err(p, x, y):
        """定义误差函数
        Args:
            p: 常数
            x: 自变量
            y: 验证因变量
        Returns:
            返回函数运算结果与验证因变量之间的误差值
        """
        return func_shape(p, x) - y

    # 定义常数的起始值，例如从 y = x + 0开始尝试，p0的取值会影响到求解效率
    p0 = [1,0]

    # 使用leastsq进行拟合
    # 此处注意args是一个元组：(自变量，因变量)，自变量和因变量都为numpy数组
    # 简单粗暴的描述就是，对于args[0]数组里的每个X，都用不同的常数进行计算，最终再跟所有的Y进行比较，得出最优的常数组合从而求解出其拟合函数
    r = leastsq(func_err, p0, args=(_font_size_np[:,0], _font_num_np))
    # 计算结果中的r[0]为一个元组，为求得的k和b
    k, b = r[0]
    # 最后我们得出结论，拟合结果为y = x
    print("k=",k,"b=",b, "r=", r)
    # 画出拟合线，以字号为X轴，函数运算结果为Y轴
    plt.plot(X,func_shape((k, b), X),color="orange",label=u"字体宽度拟合",linewidth=2) 


    plt.ylabel(u'字体大小')
    plt.xlabel(u'字号')
    plt.legend()
    plt.show()

    
if __name__ == "__main__":
    main(sys.argv)
