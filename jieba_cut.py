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

    stop_dict = []                          # stop dict
    with open('stop_words_dict.txt', 'r', encoding='utf-8') as dic:
        line = dic.readline()
        while line != "":
            line = line.rstrip('\n')
            stop_dict.append(line)
            line = dic.readline()

    out = codecs.open(out_file, 'w', 'utf-8')
    line = source.readline()
    while line!="":
        line = line.rstrip('\n')
        line.replace('\t', '').replace('\n', '').replace(' ', '')
        seg_list = list(jieba.cut(line, cut_all=False))   # cut the passage
        for word in seg_list:
            if word in stop_dict:
                seg_list.remove(word)
        output = ' '.join(seg_list)
        print(output)
        out.write(output)
        line = source.readline()
    print('END ALL')

# ----------------------------------------------------
# main


if __name__ == '__main__':
    file_path = os.getcwd() + '/lib/text_data/my_use/'
    file_list = glob.iglob(file_path + '*.txt')
    for file in file_list:
        file_name = file.split('\\')[-1]
        file_cut(file_path, file_name)

    # file_cut(file_path, '我杀了他.txt')