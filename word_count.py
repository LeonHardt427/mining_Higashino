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

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import jieba
from wordcloud import WordCloud

# ----------------------------------------
# read article
path = os.getcwd()
file_path = path + '/text_data/out_file/白马山庄杀人事件.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
segments = []
segs = jieba.cut(content)
for seg in segs:
    if len(seg) > 1:
        segments.append(seg)

df_segments = pd.DataFrame({'segment': segments})

# ----------------------------------------
# stop words dictionary

stop_words = pd.read_table('stop_words_dict.txt', sep='\\n', index_col=False, quoting=3, encoding='utf-8')
stop_words.rename(columns={'0': 'stop_word'}, inplace=True)

df_segments = df_segments[~df_segments.segment.isin(stop_words.stop_word)]

# ----------------------------------------
# count words

seg_count = df_segments.groupby(by=["segment"])["segment"].\
    agg({np.size}).rename(columns={'size': 'count'}).\
    reset_index().sort_values(['count'], ascending=False)

# ----------------------------------------
# words cloud

word_cloud = WordCloud(font_path='MSYH.TTF', background_color="white", width=1000, height=800, margin=2)
word_freq = {x[0]: x[1] for x in seg_count.head(500).values}

print(seg_count.head(100))
word_cloud_plt = word_cloud.fit_words(word_freq)
plt.imshow(word_cloud_plt)
plt.show()
