# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 10:01
# @Author  : LeonHardt
# @File    : douban_word_count.py

import os
import glob
import jieba
from word_count import word_count

if __name__ == '__main__':
    jieba.load_userdict('all_dict.txt')
    path = os.getcwd() + '/douban/out_file/'
    file_name_list = glob.iglob(path+'*.txt')
    out_file = os.getcwd() + '/lib/word_count/'
    if os.path.exists(out_file) is not True:
        os.makedirs(out_file)
    for article_name in file_name_list:
        article_name = article_name.split('\\')[-1]
        word_count(path, article_name, out_file, word_cloud=True)

