# -*- coding: utf-8 -*-
# @Time    : 2018/1/6 10:28
# @Author  : LeonHardt
# @File    : similar_word.py


import os
import pandas as pd
from gensim.models import word2vec
import matplotlib.pyplot as plt


def simliar_word(word, model, topn=20):
    """
    Parameters
    ----------
    word: str
        the word
    model: model
        word2vec model
    topn:
        the number of topn
    Returns
    -------
    """
    model_loaded = word2vec.Word2Vec.load(model)
    simliar = model_loaded.most_similar(word, topn=topn)
    return simliar


if __name__ == '__main__':
    words = ['东野圭吾', '凶手', '警察', '没有', '发现', '刀', '凶器', '老师', '眼睛', '咖啡', '侦探', '雪穗', '桐原洋介']
    model_path = os.getcwd() + '/model/Word2Vec_model/' + 'all_stop_article.model'
    for word in words:
        results = simliar_word(word, model_path, topn=10)
        name = []
        score = []
        for result in results:
            name.append(result[0])
            score.append(result[1])
            df = pd.Series(score, index=name)
        print(df)

        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['font.size'] = 18               # font_size
        plt.rcParams['axes.unicode_minus'] = False

        fig = plt.figure(figsize=(8, 6))
        plt.title(word+':相近词语挖掘', color='green', fontsize=26)
        n_group = range(len(name))
        bar_with = 0.5
        plt.bar(n_group, score, bar_with, log=True, color='purple')
        plt.xticks(n_group, name, size='small', rotation=30)
        for a, b in zip(n_group, score):
            plt.text(a, b+0.0001, '%.3f' % b, ha='center', va='bottom', fontsize=14)

        save_path = os.getcwd()+'/pic/similar_word/'
        if os.path.exists(save_path) is not True:
            os.makedirs(save_path)
        save_name = save_path + word + '.png'
        if os.path.exists(save_name) is True:
            os.remove(save_name)
        plt.savefig(save_name)

        plt.close()




