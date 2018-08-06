# -*- coding:utf-8 -*-
#__author__ = 'akers'
import getopt
import platform
import sys
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont

import configs
import operators.clipboard
import operators.image
import operators.emofile


def usage():
    print("Usage: python emofigther.py -b [background name] -f [face name] -t [texts]")

def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], "hb:f:t:", ["help"])
        print(opts)
        if(len(opts) <= 0): 
            usage()
            sys.exit()

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage()
                sys.exit()
            elif opt in ("-b", "--background"):
                bg_cmd = arg
            elif opt in ("-f", "--background"):
                face_cmd = arg
            elif opt in ("-t", "--text"):
                text = arg
    except getopt.GetoptError as err:
        print("参数解析出错：", err)
        usage()
        sys.exit()

    # 创建表情图
    image = operators.image.draw_emo(operators.emofile.get_bg_path(bg_cmd), operators.emofile.get_face_path(face_cmd), text)
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
