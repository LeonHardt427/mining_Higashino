# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 12:48
# @Author  : LeonHardt
# @File    : similiar_document.py

import os
import glob
import numpy as np
from gensim import corpora, models, similarities
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


path = os.getcwd()+'/lib/text_data/out_file/'
name = []
name_list = glob.iglob(path+'*.txt')
for name_text in name_list:
    name_str = name_text.split('\\')[-1].split('.')[0]
    name.append(name_str)
print(name)

path = os.getcwd()+'/model/Doc2Vec_model/'
dictionary = corpora.Dictionary.load(path+'doc_dic_filter.dict')

corpus = corpora.MmCorpus(path+'doc_dic_filter.mm')


tfidf_model = models.TfidfModel(corpus)
corpus_tfidf = tfidf_model[corpus]

lsi_model = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=3)
corpus_lsi = lsi_model[corpus_tfidf]


plt.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

name_list_remove = []


# -----------------------------------------------------------
# 2D  —————— n_topics=2

# fig = plt.figure()
# X = []
# y = []
# for index, lsi in enumerate(corpus_lsi):
#     if (lsi == []) is True:
#         name_list_remove.append(name[index])
#     else:
#         X.append(lsi[0][1])
#         y.append(lsi[1][1])
#     # print(lsi)
# print(name_list_remove)
# # X = np.array(X)
# # y = np.array(y)
# for text in name_list_remove:
#     name.remove(text)
# for num in range(len(X)):
#     plt.scatter(X[num], y[num], s=100)
#     plt.text(X[num], y[num] + 0.02, '{}'.format(name[num]))
# plt.title('东野圭吾作品二维LSI分布', color='black', fontsize=26)
# plt.show()

# -----------------------------------------------------------
# # 3D  —————— n_topics=3
# figure = plt.figure()
# ax = plt.subplot(111, projection='3d')
# X = []
# y = []
# z = []
# for index, lsi in enumerate(corpus_lsi):
#     if (lsi == []) is True:
#         name_list_remove.append(name[index])
#     else:
#         X.append(lsi[0][1])
#         y.append(lsi[1][1])
#         z.append(lsi[2][1])
#     # print(lsi)
# print(name_list_remove)
# # X = np.array(X)
# # y = np.array(y)
# for text in name_list_remove:
#     name.remove(text)
# for num in range(len(X)):
#     ax.scatter(X[num], y[num], z[num], s=100)
#     ax.text(X[num], y[num] + 0.02, z[num], '{}'.format(name[num]))
# plt.title('东野圭吾作品三维LSI分布', color='black', fontsize=26)
# ax.set_zlabel('topics=1')
# ax.set_ylabel('topics=2')
# ax.set_xlabel('topics=3')
# plt.show()

# --------------------------------------------
# eyi------------similarity

eyi_corpus = corpora.MmCorpus(path+'eyi_dic_filter.mm')

eyi_model = models.TfidfModel(eyi_corpus)
eyi_tfidf = tfidf_model[eyi_corpus]

lsi_model = models.LsiModel(eyi_tfidf, id2word=dictionary, num_topics=3)
eyi_lsi = lsi_model[eyi_tfidf]

index = similarities.MatrixSimilarity(corpus_lsi)
sim = index[eyi_lsi][0]

np.savetxt(path+'eyi_sim.txt', sim, delimiter=',')
print(sim)
#
# for i in sim:
#     print(i.shape()
# sim = sim.reshape((-1, 1))
# sim_sort = sim.copy()
# # print(sim)
# index_sort = np.argsort(sim, axis=-1)
# # print(sim)
# # print(type(index_sort))
# print(index_sort)
# print(sim)
# simila_index = index_sort[-6:-1]
# # print(simila_index)
# # for i in simila_index:
# #     print(i)
#     print(sim[0][simila_index])