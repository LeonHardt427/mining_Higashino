# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 21:05
# @Author  : LeonHardt
# @File    : place_count.py

import os
import pandas as pd
import matplotlib.pyplot as plt

path = os.getcwd()+'/lib/word_count/all_stop_article.csv'
place_path = os.getcwd()+'/lib/all_places.txt'
place_list = []
with open(place_path, 'r', encoding='utf-8') as place:
    lines = place.readlines()
    for line in lines:
        line = line.strip('\n')
        if (line in place_list) is not True:
            place_list.append(line)


df = pd.read_csv(path, sep=',', encoding='utf-8', engine='python')
df = df.set_index('segment').drop(df.columns[0], axis=1)

place_summary = {}
for name in place_list:
    if name in df.index:
        place_summary[name] = int(df.loc[name].values)

place_summary = pd.Series(place_summary)
p = place_summary.sort_values(ascending=False)

plt.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

p.head(20).plot('bar')
plt.xticks(range(20), p.head(20).index, rotation=30, size=12)
plt.title('东野圭吾作品地名统计', color='black', fontsize=26)
plt.show()
print(p)
