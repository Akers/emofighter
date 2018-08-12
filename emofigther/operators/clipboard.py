# -*- coding:utf-8 -*-
#__author__ = 'akers'
import win32clipboard as clip
import sys
import platform
import win32con

def add_bmp(bytes_io):
    """bmp位图放入Windows剪贴板中
    Args:
        bytes_io: 从图片中获取的字节流，使用image.save(output, format="BMP")可将Image写入到字节流中

    Returns:

    Raises:

    """
    if 'Windows' in platform.platform() or 'windows' in platform.platform():
        clip.OpenClipboard()  # 打开剪贴板
        clip.EmptyClipboard()  # 先清空剪贴板
        data = bytes_io.getvalue()[14:]
        clip.SetClipboardData(win32con.CF_DIB, data)  # 将图片放入剪贴板
        clip.CloseClipboard()
