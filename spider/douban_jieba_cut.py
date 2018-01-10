# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 9:55
# @Author  : LeonHardt
# @File    : douban_jieba_cut.py

import os
import glob
from jieba_cut import file_cut

if __name__ == '__main__':
    file_path = os.getcwd() + '/douban/'
    file_list = glob.iglob(file_path + '*.txt')
    for file in file_list:
        file_name = file.split('\\')[-1]
        file_cut(file_path, file_name)

