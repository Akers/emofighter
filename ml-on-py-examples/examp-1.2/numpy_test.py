# -*- coding:utf-8 -*-
#__author__ = 'akers'
import numpy as np

print('使用列表生成一维数组')
data = [1,2,3,4,5,6]
x = np.array(data)
print(x) #打印数组
print(x.dtype) #打印数组元素的类型

print('使用列表生成二维数组')
data = [[1,2],[3,4],[5,6]]
x = np.array(data)
print(x) #打印数组
print(x.ndim) #打印数组的维度
print(x.shape) #打印数组各个维度的长度。shape是一个元组

print(x[:])