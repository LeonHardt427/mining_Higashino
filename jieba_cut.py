# -*- coding: utf-8 -*-
# @Time    : 2018/1/2 20:37
# @Author  : LeonHardt
# @File    : jieba_cut.py


import os
import glob
import codecs


import jieba
import jieba.analyse

# -------------------------------------------
# file direction set
# load user_dict
# -------------------------------------------
jieba.load_userdict('all_dict.txt')


# ------------------------------------------
# article cut


def file_cut(path, data_name):
    """
    Parameters
    ----------
    path: str
        file path
    data_name:
        text name

    Returns
    -------
    None
    cut the passage and write
    """
    source_file = path + '/' + data_name    # data name
    source = codecs.open(source_file, 'r', encoding='utf-8')

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
        seg_list = jieba.cut(line, cut_all=False)   # cut the passage
        output = ' '.join(list(seg_list))
        print(output)
        print('-------------------------')
        out.write(output + '\r\n')
        line = source.readline()

    print('END ALL')

# ----------------------------------------------------
# main


if __name__ == '__main__':
    file_path = os.getcwd() + '/text_data/'
    file_list = glob.iglob(file_path + '*.txt')
    for file in file_list:
        file_name = file.split('\\')[-1]
        file_cut(file_path, file_name)

