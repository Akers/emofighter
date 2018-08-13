# -*- coding:utf-8 -*-
#__author__ = 'akers'
import argparse
import getopt
import platform
import sys
from getopt import getopt
from io import BytesIO

import cv2

from PIL import Image, ImageDraw, ImageFont

import configs
import operators.clipboard
import operators.image


def main(argv):
    args = menu()
    bgPath = list(filter(lambda i: i["name"] == args.background, configs.CONFIGS["emo"]["backgrounds"]))
    facePath = list(filter(lambda i: i["name"] == args.face, configs.CONFIGS["emo"]["faces"]))
    bgPath = bgPath[0]["path"] if len(bgPath) > 0 else configs.CONFIGS["emo"]["backgrounds"][0]["path"]
    facePath = facePath[0]["path"] if len(facePath) > 0 else configs.CONFIGS["emo"]["faces"][0]["path"]
    text = args.text
    image = operators.image.draw_emo_v2(bgPath, facePath, text)
    # 创建表情图
    output = BytesIO()
    image.save(output, format="BMP")
    operators.clipboard.add_bmp(output)
    image.save('output/facing.png')
    # plt.figure("生成表情包")
    # plt.imshow(target)
    # plt.show()

def menu():
    """CLI菜单定义
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--face", help="select the face in [awkward|diss|laugth|smail]")
    parser.add_argument("-bg", "--background", help="select the background in [cry|default|doubt|point]")
    parser.add_argument("-t", "--text", help="the text on emoticon")    
    return parser.parse_args()

if __name__ == "__main__":
    main(sys.argv)
