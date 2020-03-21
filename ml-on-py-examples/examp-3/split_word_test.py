# -*- coding:utf-8 -*-
#__author__ = 'akersliang@gmail.com'
# NLP第一步，分词
import jieba
import jieba.posseg as pseg
import sys



def test_thulac(text):
    words = pseg.cut(text)
    print("jieba分词：")
    for word, flag in words:
        print('%s_%s' % (word, flag))
    return

if __name__ == "__main__":
    test_thulac(sys.argv[1])