# -*- coding:utf-8 -*-
#__author__ = 'akers'

import sys #包导入

# 常见的main函数定义
def main(argv=[]):
    print("hellow world: ", argv)


# 你看不到我，你看不到我
if __name__ == "__main__":
    main(sys.argv) # sys.argv获取命令行参数
