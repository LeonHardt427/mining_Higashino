# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 13:22
# @Author  : LeonHardt
# @File    : main_characters.py

import os
import glob

import pandas as pd
import matplotlib.pyplot as plt


# ----------------------------------------------------------------
# main character function
def main_character(source_path, file_name, name_list_path, out_path):
    """
    Parameters
    ----------
    source_path: /..../
        source path of csv
    file_name:  *.csv   (without .csv)
        file name of csv
    out_path: /...../
        out path of figure
    name_list_path: *.txt
        main character txt
    Returns
    -------
        None
        save main character fig in out_path
    """
    path = source_path + file_name + '.csv'
    a = pd.read_csv(path, encoding='utf-8', engine='python')
    a = a.drop([a.columns[0]], axis=1).set_index('segment')
    path = name_list_path + file_name + '.txt'
    with open(path, encoding='utf-8') as file:
        name_list = []
        line = file.readline().rstrip("\n")
        while line != "":
            name_list.append(line)
            line = file.readline().rstrip("\n")
    name_count = {}
    for name in name_list:
        if name in list(a.index):
            name_count[name] = a.loc[name, 'count']
            print(name + " count is " + str(a.loc[name, 'count']))
        else:
            print(name + " is not found!")

    df_name_count = pd.Series(name_count).sort_values(ascending=False)

    # -------------------------------------
    # bar figure
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.size'] = 14               # font_size
    plt.rcParams['figure.figsize'] = (8, 6)     # fig_size
    df_name_count.head(10).sort_values(ascending=True).plot(kind='barh')
    plt.title(file_name+'主角光环', fontsize=20, fontweight='bold', color='blue')
    out_path = os.getcwd() + '/main_character/'
    if os.path.exists(out_path) is not True:
        os.makedirs(out_path)
    out_figure = out_path + file_name + '.png'
    if os.path.exists(out_figure) is True:
        os.remove(out_figure)
    plt.savefig(out_figure)
    # plt.show()
    plt.close()


if __name__ == '__main__':
    soure_path = os.getcwd() + '/word_count/'
    name_list = os.getcwd() + '/name_dict/'
    out_path = os.getcwd() + '/main_character/'
    article_list = glob.iglob(soure_path+'*.csv')
    for article in article_list:
        name = article.split('\\')[-1].split('.')[0]
        main_character(source_path=soure_path, file_name=name, name_list_path=name_list, out_path=out_path)

