# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 12:55
# @Author  : LeonHardt
# @File    : word_count.py
"""
function:
    count words and draw word-cloud
from:
    ~/text_data/out_file/*.txt   (already cut)
to:
    ~/word_cloud/*.png
"""
import os
import glob

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import jieba
from wordcloud import WordCloud

# -------------------------------------------------------------------------------------
# word count function


def word_count(file_path, file_name, out_path, stop_word='stop_words_dict.txt', word_cloud=False):
    """
    Function
    ----------
        count the number of articles
    Parameters
    ----------
    file_path:
        the path to get the articles (already cut)
    file_name:
        the name of the file
    out_path:
        the file name of output
    stop_word: *txt
        stop_word dictionary
    word_cloud: bool
        need word cloud or not
    Returns
    -------
        None
        save the count result in output file as '*.csv'
    """
    # read article
    file_path = file_path + file_name
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    segments = []
    segs = jieba.cut(content)
    for seg in segs:
        if len(seg) > 1:
            segments.append(seg)

    df_segments = pd.DataFrame({'segment': segments})

    # stop words dictionary
    stop_words = pd.read_table(stop_word, sep='\\n', index_col=False, quoting=3, encoding='utf-8')
    stop_words.rename(columns={'0': 'stop_word'}, inplace=True)

    df_segments = df_segments[~df_segments.segment.isin(stop_words.stop_word)]

    # count words
    seg_count = df_segments.groupby(by=["segment"])["segment"].\
        agg({np.size}).rename(columns={'size': 'count'}).\
        reset_index().sort_values(['count'], ascending=False)
    out_file_name = out_path + file_name.split('.')[0]+'.csv'
    if os.path.exists(out_file_name) is True:
        os.remove(out_file_name)
    seg_count.to_csv(out_file_name)

# -----------------------------------------------------------------------------
# words cloud function
    if word_cloud is True:
        word_cloud_pic = WordCloud(font_path='fz.TTF', background_color="white", width=2000, height=1500, margin=2)
        word_freq = {x[0]: x[1] for x in seg_count.head(100).values}
        print(seg_count.head(100))
        word_cloud_plt = word_cloud_pic.fit_words(word_freq)
        plt.axis('off')               # close axis
        plt.imshow(word_cloud_plt)
        cloud_path = os.getcwd() + '/pic/word_cloud/'
        if os.path.exists(cloud_path) is not True:
            os.makedirs(cloud_path)
        out_file_name = cloud_path + file_name.split('.')[0] + '.png'
        if os.path.exists(out_file_name) is True:
            os.remove(out_file_name)
        plt.savefig(out_file_name)
        # plt.show()
        plt.close()


if __name__ == '__main__':
    path = os.getcwd() + '/lib/text_data/out_file/all/'
    file_name_list = glob.iglob(path+'*.txt')
    out_file = os.getcwd() + '/lib/word_count/'
    if os.path.exists(out_file) is not True:
        os.makedirs(out_file)
    for article_name in file_name_list:
        article_name = article_name.split('\\')[-1]
        word_count(path, article_name, out_file, word_cloud=True)





