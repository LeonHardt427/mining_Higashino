# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 20:52
# @Author  : LeonHardt
# @File    : all_article_cut.py

import os
import glob
import codecs

import jieba

path = os.getcwd() + '/lib/text_data/out_file/all/'
if os.path.exists(path) is not True:
    os.makedirs(path)

if os.path.exists(path+'all_article.txt') is not True:
    # ----------------------------------------------------------------------------------
    # cut all article
    file_path = os.getcwd() + '/lib/text_data/out_file/'
    file_name_list = glob.iglob(file_path + '*.txt')
    # --------------------------------------
    # stop words dictionary   (word2vec not use stop_dict)
    # stop_dict = []
    # with open('stop_words_dict.txt', 'r', encoding='utf-8') as dic:
    #     line = dic.readline()
    #     while line != "":
    #         line = line.rstrip('\n')
    #         stop_dict.append(line)
    #         line = dic.readline()
    # ---------------------------------------
    # cut without stop_word
    jieba.load_userdict('all_dict.txt')
    output_path = path + 'all_article.txt'
    if os.path.exists(output_path) is True:
        os.remove(output_path)
    out = codecs.open(output_path, 'w', 'utf-8')
    for file in file_name_list:
        print("deal：{}".format(file))
        with codecs.open(file, encoding="utf8") as f:
            lines = f.readlines()
            for line in lines:
                # line = line.rstrip('\n')
                line.replace('\t', '').replace('\n', '').replace(' ', '')
                words = jieba.cut(line, cut_all=False)
                output = ' '.join(words)
                out.write(output)

    # ---------------------------------------
    # cut without stop_word
if os.path.exists(path+'all_stop_article.txt') is not True:
    # ----------------------------------------------------------------------------------
    # cut all article
    file_path = os.getcwd() + '/lib/text_data/out_file/'
    file_name_list = glob.iglob(file_path + '*.txt')
    # --------------------------------------
    # stop words dictionary   (word2vec not use stop_dict)
    stop_dict = []
    with open('stop_words_dict.txt', 'r', encoding='utf-8') as dic:
        line = dic.readline()
        while line != "":
            line = line.rstrip('\n')
            stop_dict.append(line)
            line = dic.readline()
    # ---------------------------------------
    # cut without stop_word
    jieba.load_userdict('all_dict.txt')
    output_path = path + 'all_stop_article.txt'
    if os.path.exists(output_path) is True:
        os.remove(output_path)
    out = codecs.open(output_path, 'w', 'utf-8')
    for file in file_name_list:
        print("deal：{}".format(file))
        with codecs.open(file, encoding="utf8") as f:
            lines = f.readlines()
            for line in lines:
                # line = line.rstrip('\n')
                line.replace('\t', '').replace('\n', '').replace(' ', '')
                words = list(jieba.cut(line, cut_all=False))
                for word in words:
                    if word in stop_dict:
                        words.remove(word)
                output = ' '.join(words)
                out.write(output)
                # for word in words:
                #     if (word in stop_dict) is not True:
