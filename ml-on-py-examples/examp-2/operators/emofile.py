# 表情文件及路径相关操作模块
#
# -*- coding:utf-8 -*-
#__author__ = 'akers'

import configs


def get_face_path(face_cmd):
    """根据配置中的command获取表情文件path，如果给出的cmd查找不到文件，则默认返回配置中的第一个表情
    Args:
        face_cmd 表情指令，对应configs文件中的command配置
    """
    faces = configs.CONFIGS["emo"]["faces"]
    fl = list(filter(lambda it: it["command"] == face_cmd, faces))
    fl = faces if len(fl) <= 0 else fl
    return fl[0]["path"]

def get_bg_path(bg_cmd):
    """根据配置中的command获取北京文件path，如果给出的cmd查找不到文件，则默认返回配置中的第一个
    Args:
        bg_cmd 北京指令，对应configs文件中的command配置
    """
    bgs = configs.CONFIGS["emo"]["backgrounds"]
    fl = list(filter(lambda it: it["command"] == bg_cmd, bgs))
    fl = bgs if len(fl) <= 0 else fl
    return fl[0]["path"]