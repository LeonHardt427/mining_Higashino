# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 21:07
# @Author  : LeonHardt
# @File    : unsupervised_anaylsis_lda.py

import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

path = os.getcwd()+'/lib/text_data/out_file/'
name = []
name_list = glob.iglob(path+'*.txt')
for name_text in name_list:
    name_str = name_text.split('\\')[-1].split('.')[0]
    name.append(name_str)

save_path = os.getcwd()+'/model/Doc2Vec_model/corpus_np_lda.txt'
lda = np.loadtxt(save_path, delimiter=',')
y = np.arange(56)

# ---------------------------------------------------------------------
# PCA
# pca = PCA(n_components=3)
# lda_pca = pca.fit_transform(lda)
#
# plt.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
# # ===========================================
# # 2D
# fig = plt.figure()
# ax = plt.subplot(111, projection='3d')
# for index, X in enumerate(lda_pca):
#     ax.scatter(X[0], X[1], X[2], s=100)
#     # ax.text(X[0], X[1] + 0.02, X[2], '{}'.format(name[index]))
# plt.title('东野圭吾作品LDA(200)-PCA', color='black', fontsize=26)
# plt.xlabel('PCA1', size='large')
# # plt.ylabel('PCA2', size='large')
# # plt.zlabel('PCA2', size='large')
# plt.show()

# ---------------------------------------------------------------------
# KMeans
km = KMeans(n_clusters=5, init='random',n_init=10, max_iter=300, random_state=0)
y_km = km.fit_predict(lda)
print(y_km)
# print(y_km.shape)
result = {}
for index, kmm in enumerate(y_km):
    result[name[index]] = kmm
    # if kmm != 1 :
    #     print(name[index]+' is '+ str(kmm))

result = pd.Series(result)
print(result)
result.to_excel( os.getcwd()+'/model/kmeans.xls')