# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 20:55
# @Author  : LeonHardt
# @File    : key_words.py

"""
function:
    find key words
from :
    ~/text_data/out_file/*.txt  (already cut)
to:
    None
"""
import os
import numpy as np
import jieba.analyse


path = os.getcwd() + '/text_data/out_file/'
name = '白马山庄杀人事件.txt'
stop_dict = []
with open('stop_words_dict.txt', 'r', encoding='GBK') as stopwords:
    stop_list = stopwords.readline()
    while stop_list != "":
        stop_list = stop_list.rstrip('\n')
        stop_dict.append(stop_list)
        stop_list = stopwords.readline()
    print(stop_dict)

