# -*- coding: utf-8 -*-
# @Time    : 2017/12/26 19:54
# @Author  : LeonHardt
# @File    : jieba_test.py

import os
import sys
import codecs
import re
import jieba
import jieba.analyse

# -------------------------------------------
# file direction set
# load user_dict
# -------------------------------------------
jieba.load_userdict('my_dict.txt')

file_path = os.getcwd() + '/text_data/'
file_name = '《再一个谎言》之 寒冷的灼热.txt'

# ------------------------------------------
# Test
# ------------------------------------------

# text = "我来自浙江大学，是浙江大学的学生"
# seg_list = jieba.cut(text, cut_all=True)
# print("全模式：" + ','.join(seg_list))
#
# text = "我来自浙江大学，是浙江大学的学生"
# seg_list = jieba.cut(text, cut_all=False)
# print("全模式：" + ','.join(seg_list))

# ------------------------------------------
# article cut
# ------------------------------------------


def read_file_cut(path, data_name):

    """
    read files and cut
    :return: None
    """

    source_file = path + '/' + data_name
    source = open(source_file, 'r')

    out_path = path + '/out_file/'
    if os.path.exists(out_path) is not True:
        os.makedirs(out_path)

    out_file = out_path + data_name
    if os.path.exists(out_file):
        os.remove(out_file)

    out = codecs.open(out_file, 'w', 'utf-8')
    line = source.readline()
    line = line.rstrip('\n')
    while line!="":
        seg_list = jieba.cut(line, cut_all=False)
        output = ' '.join(list(seg_list))
        print(output)
        print('-------------------------')
        out.write(output + '\r\n')
        line = source.readline()

    print('END ALL')


if __name__ == '__main__':
    read_file_cut(file_path, file_name)






