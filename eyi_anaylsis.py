# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 19:11
# @Author  : LeonHardt
# @File    : eyi_anaylsis.py


import os
import glob
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------
# anaylsis eyi
path = os.getcwd()+'/lib/text_data/out_file/'
name = []
name_list = glob.iglob(path+'*.txt')
for name_text in name_list:
    name_str = name_text.split('\\')[-1].split('.')[0]
    name.append(name_str)
print(name)

model_path = os.getcwd()+'/model/Doc2Vec_model/'
eyi_list = np.loadtxt(model_path+'eyi_sim.txt', delimiter=',')

plt.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
n_group = 7
name_list_sort = []
X = []
bar_with = 0.5
sort_index = np.argsort(-eyi_list, axis=-1)[0: n_group]
for i in sort_index:
    name_list_sort.append(name[i])
    X.append(eyi_list[i])

plt.title('恶意最相近文章', color='black', fontsize=26)
plt.bar(range(n_group), X, bar_with, log=True)
plt.xticks()
plt.xticks(range(n_group), name_list_sort, size='large', rotation=30)
for i in range(n_group):
    plt.text(i-0.25, X[i]+0.01, '%.3f' % X[i], size='large')
plt.show()

