# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 13:38
# @Author  : LeonHardt
# @File    : emotion_summary.py

import os
import glob
import numpy as np
import matplotlib.pyplot as plt

path = os.getcwd()+'/lib/emotion/'
score_list = glob.iglob(path+'*.txt')
name_list = []
score_mean = []
score_std = []
for file in score_list:
    name_list.append(file.split('\\')[-1].split('.')[0])
    score = np.loadtxt(file, delimiter=',')
    score_mean.append(score.mean())
    score_std.append(score.std())

print(name_list)
print(score_mean)
print(score_std)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.size'] = 18  # font_size
plt.rcParams['axes.unicode_minus'] = False

score_mean = np.array(score_mean)
score_std = np.array(score_std)
index = np.argsort(-score_mean, axis=-1)
fig = plt.figure(figsize=(8, 6))
bar_with = 0.5
name_list_sort = []
for num, i in enumerate(index):
    plt.bar(num, score_mean[i], bar_with, log=True)
    plt.text(num-0.4, score_mean[i]+0.005, '%.3f' % score_mean[i], size='small', color='black')
    name_list_sort.append(name_list[i])
plt.title('豆瓣书评东野圭吾作品评价情感分析', color='black', fontsize=26)
plt.xticks(range(len(name_list_sort)), name_list_sort, size='small', rotation=30)
plt.show()