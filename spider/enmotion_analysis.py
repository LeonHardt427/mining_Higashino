# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 10:17
# @Author  : LeonHardt
# @File    : enmotion_analysis.py

import os
import glob
import snownlp
import numpy as np

path = os.getcwd() + '/douban/'
f_list = glob.iglob(path+'*.txt')
for file in f_list:
    result = []
    with open(file, 'r', encoding='utf-8') as f:
        name = file.split('\\')[-1]
        line = f.readline()
        while line!="":
            senti = snownlp.SnowNLP(line)
            senti_score = senti.sentiments
            result.append(senti_score)
            line = f.readline()
        score = np.array(result)
        score_path = os.getcwd()+'/lib/emotion/'
        if os.path.exists(score_path) is not True:
            os.makedirs(score_path)
        score_name = score_path + name
        if os.path.exists(score_name) is True:
            os.remove(score_name)
        np.savetxt(score_name, result, delimiter=',')
        print(name+' is down')