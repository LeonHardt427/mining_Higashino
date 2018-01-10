
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 20:20
# @Author  : LeonHardt
# @File    : douban_doc_vec.py


import os
import glob

import logging
import jieba
from gensim import corpora


jieba.load_userdict('all_dict.txt')


def tokenization(file_name, stop_dict):
    result = []
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line.replace('\t', '').replace('\n', '').replace(' ', '')
            words = jieba.cut(line, cut_all=False)
            for word in words:
                if (word in stop_dict) is not True:
                    if word != ' ' and word != "\u3000" and word != "\n":
                        result.append(word)
    return result


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
    stop_dict = []
    with open('stop_words_dict.txt', 'r', encoding='utf-8') as dic:
        line = dic.readline()
        while line != "":
            line = line.rstrip('\n')
            stop_dict.append(line)
            line = dic.readline()

# -------------------------------------------------------------
    # ALL artcle

    path = os.getcwd()+'/douban/out_file/'
    corpus = []
    documents = glob.iglob(path+'*.txt')
    for document in documents:
        corpus.append(tokenization(document, stop_dict))
        print(document+'is ready')
    print(corpus)
    print(type(corpus))

    dictionary = corpora.Dictionary(corpus)
    print(len(dictionary))
    dictionary.filter_extremes(no_below=5, keep_n=100000)
    print(len(dictionary))
#
    doc_2_vec = os.getcwd() + '/model/Doc2Vec_model/'
    if os.path.exists(doc_2_vec) is not True:
        os.makedirs(doc_2_vec)
    if os.path.exists(doc_2_vec+'douban_doc_filter.dict') is True:
        os.remove(doc_2_vec+'douban_doc_filter.dict')
    dictionary.save(doc_2_vec+'douban_doc_filter.dict')

    doc_vectors = [dictionary.doc2bow(text) for text in corpus]
    if os.path.exists(doc_2_vec+'douban_doc_filter.mm') is True:
        os.remove(doc_2_vec+'douban_doc_filter.mm')
    corpora.MmCorpus.serialize(doc_2_vec+'douban_doc_filter.mm', doc_vectors)

# # -----------------------------------
# eyi
#     all_path = os.getcwd() + '/model/Doc2Vec_model/'
#     dictionary = corpora.Dictionary.load(all_path + 'doc_dic_filter.dict')
#
#     path = os.getcwd()+'/lib/text_data/out_file/'
#     eyi = []
#     documents = path+'恶意.txt'
#     eyi.append(tokenization(documents, stop_dict))
#
#     doc_2_vec = os.getcwd() + '/model/Doc2Vec_model/'
#     doc_vectors = [dictionary.doc2bow(text) for text in eyi]
#     if os.path.exists(doc_2_vec+'eyi_dic_filter.mm') is True:
#         os.remove(doc_2_vec+'eyi_dic_filter.mm')
#     corpora.MmCorpus.serialize(doc_2_vec+'eyi_dic_filter.mm', doc_vectors)
