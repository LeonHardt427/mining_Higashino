# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 17:25
# @Author  : LeonHardt
# @File    : all_vec_anaylsis.py

import os
import logging
from gensim.models import word2vec

Pattern = "stop"
"""
train all article model
"""
if Pattern == "all":
    logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
    path = os.getcwd() + '/text_data/out_file/all/all_article.txt'
    sentences = word2vec.Text8Corpus(path)
    model = word2vec.Word2Vec(sentences, size=200)
    out_model_path = os.getcwd()+'/Word2Vec_model/'
    if os.path.exists(out_model_path) is not True:
        os.makedirs(out_model_path)
    out_model = out_model_path + path.split('/')[-1].split('.')[0] + '.model'
    model.save(out_model)
else:
    logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
    path = os.getcwd() + '/text_data/out_file/all/all_stop_article.txt'
    sentences = word2vec.Text8Corpus(path)
    model = word2vec.Word2Vec(sentences, size=200)
    out_model_path = os.getcwd()+'/Word2Vec_model/'
    if os.path.exists(out_model_path) is not True:
        os.makedirs(out_model_path)
    out_model = out_model_path + path.split('/')[-1].split('.')[0] + '.model'
    model.save(out_model)
