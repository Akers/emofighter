# -*- coding:utf-8 -*-
#__author__ = 'akers'
import argparse
import getopt
import platform
import sys
import os
from getopt import getopt
from io import BytesIO

import cv2

from PIL import Image, ImageDraw, ImageFont

import configs
import operators.clipboard
import operators.image
import operators.emofile


def main(argv):
    args = menu()
    bg_path = operators.emofile.get_bg_path(args.background)
    face_path = operators.emofile.get_face_path(args.face)
    text = args.text
    image = operators.image.draw_emo(bg_path, face_path, text)
    # 创建表情图
    output = BytesIO()
    image.save(output, format="BMP")
    operators.clipboard.add_bmp(output)
    not os.path.exists('output') and os.mkdir("output")
    image.save('output/facing.png')
    # plt.figure("生成表情包")
    # plt.imshow(target)
    # plt.show()

def menu():
    """CLI菜单定义
    """
    parser = argparse.ArgumentParser()
    bg_config_cmds = list(map(lambda x: x["command"], configs.CONFIGS["emo"]["backgrounds"]))
    faces_config_cmds = list(map(lambda x: x["command"], configs.CONFIGS["emo"]["faces"]))

    # 可选参数
    parser.add_argument("-f", "--face"
    , choices=faces_config_cmds
    , help="select the face to use")
    parser.add_argument("-bg", "--background"
    , choices=bg_config_cmds
    , help="select the background to use")
    # 必须参数
    requiredNamed = parser.add_argument_group('required arguments')
    requiredNamed.add_argument("-t", "--text", help="the text on emoticon", required=True)
    return parser.parse_args()

if __name__ == "__main__":
    main(sys.argv)
