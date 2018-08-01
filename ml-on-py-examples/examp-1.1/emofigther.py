# -*- coding:utf-8 -*-
#__author__ = 'akers'
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import sys,platform,operators.image,operators.clipboard


def main(argv):
    # 创建表情图
    image = operators.image.draw_emo('./resources/background/pander/default.png', './resources/face/jgz/laugth.png', argv[1])
    output = BytesIO()
    image.save(output, format="BMP")
    operators.clipboard.add_bmp(output)
    image.save('output/facing.png')

    # 调试用
    # plt.figure("生成表情包")
    # plt.imshow(target)
    # plt.show()

if __name__ == "__main__":
    main(sys.argv)
