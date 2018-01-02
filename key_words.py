# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 20:55
# @Author  : LeonHardt
# @File    : key_words.py

import os
import numpy as np
import jieba.analyse


path = os.getcwd() + '/text_data/out_file/'
name = '《再一个谎言》之 寒冷的灼热.txt'
stop_dict = []
with open('stop_words_dict.txt', 'r', encoding='GBK') as stopwords:
    stop_list = stopwords.readline()
    while stop_list != "":
        stop_list = stop_list.rstrip('\n')
        stop_dict.append(stop_list)
        stop_list = stopwords.readline()
    print(stop_dict)

# file_name = path + name
# source = open(file_name, 'r', encoding='utf-8')
# a = source.read()
#
#
# print(a)
#
# tags = jieba.analyse.extract_tags(a, topK=3)
# print(tags)

