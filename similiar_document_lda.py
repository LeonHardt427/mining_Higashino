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
print(len(name))

model_path = os.getcwd()+'/model/Doc2Vec_model/'
dictionary = corpora.Dictionary.load(model_path+'doc_dic_filter.dict')

corpus = corpora.MmCorpus(model_path+'doc_dic_filter.mm')


tfidf_model = models.TfidfModel(corpus)
corpus_tfidf = tfidf_model[corpus]

lda_model = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=200)
corpus_lda = lda_model[corpus_tfidf]


plt.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

name_list_remove = []


# -----------------------------------------------------------
# 2D  —————— n_topics=2

# fig = plt.figure()
# X = []
# y = []
# for index, lda in enumerate(corpus_lda):
#     if (lda == []) is True:
#         name_list_remove.append(name[index])
#     else:
#         X.append(lda[0][1])
#         y.append(lda[1][1])
#     # print(lsi)
# print(name_list_remove)
# # X = np.array(X)
# # y = np.array(y)
# for text in name_list_remove:
#     name.remove(text)
# for num in range(len(X)):
#     plt.scatter(X[num], y[num], s=100)
#     # plt.text(X[num], y[num] + 0.02, '{}'.format(name[num]))
# plt.title('东野圭吾作品二维LDA分布', color='black', fontsize=26)
# plt.show()

# -----------------------------------------------------------
# 3D  —————— n_topics=3
# figure = plt.figure()
# ax = plt.subplot(111, projection='3d')
# X = []
# y = []
# z = []
# for index, lda in enumerate(corpus_lda):
#     if (lda == []) is True:
#         name_list_remove.append(name[index])
#     else:
#         X.append(lda[0][1])
#         y.append(lda[1][1])
#         z.append(lda[2][1])
#     # print(lsi)
# print(name_list_remove)
# # X = np.array(X)
# # y = np.array(y)
# for text in name_list_remove:
#     name.remove(text)
# for num in range(len(X)):
#     ax.scatter(X[num], y[num], z[num], s=100)
#     ax.text(X[num], y[num] + 0.02, z[num], '{}'.format(name[num]))
# plt.title('东野圭吾作品三维LDA分布', color='black', fontsize=26)
# ax.set_zlabel('topics=1')
# ax.set_ylabel('topics=2')
# ax.set_xlabel('topics=3')
# plt.show()

# -------------------------------------------------------------------
#  topics = 200
for i in corpus_lda:
    print(i)
corpus_np_lda_200 = np.zeros((56, 200))

for index, num in enumerate(corpus_lda):
    for temp in range(len(num)):
        corpus_np_lda_200[index][num[temp][0]] = num[temp][1]

save_path = os.getcwd()+'/model/Doc2Vec_model/corpus_np_lda.txt'
if os.path.exists(save_path) is True:
    os.remove(save_path)
np.savetxt(save_path, corpus_np_lda_200, delimiter=',')

