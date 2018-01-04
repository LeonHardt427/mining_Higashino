# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 19:24
# @Author  : LeonHardt
# @File    : creat_name_dict.py
"""
function:
    create name dictionary of every article
from:
    ~/attrs/names.txt
to:
    ~/name_dict/*.txt
"""
import os
import glob

path = os.getcwd()
source_path = path + '/attrs/*.txt'
# source_path = path + '/attrs/*name.txt'   # only name dictionary

output_path = path + '/name_dict/'
if os.path.exists(output_path) is not True:
    os.makedirs(output_path)

file_list = glob.iglob(source_path)
# ---------------------------------------------------------------------
"""only name dictionary and separated
"""

# with open(source_path, 'r', encoding='utf-8') as f_name:
#     line = f_name.readline()
#     while line != "":
#         name_dict = line.rstrip("\n")
#         print("txt_name: " + name_dict + ' is done')
#         name_txt = output_path + line.rstrip("\n") + '.txt'
#         if os.path.exists(name_txt) is True:
#             os.remove(name_txt)
#
#         line = f_name.readline().rstrip("\n")
#         line = line.replace(" ", "\n")
#         with open(name_txt, 'w', encoding='utf-8') as dict:
#             dict.write(line)
#         line = f_name.readline()

# ---------------------------------------------------------------------
"""make whole dictionary
"""

name_txt = 'all_name_dict.txt'
with open(name_txt, 'w', encoding='utf-8') as dict:
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f_name:
            line = f_name.readline()
            while line != "":
                name_dict = line.rstrip("\n")
                print("txt_name: " + name_dict + ' is done')

                line = f_name.readline().rstrip("\n")
                line = line.replace(" ", "\n")
                dict.write(line)
                line = f_name.readline()

