#-*- coding:utf-8 -*-

from snownlp import SnowNLP
from snownlp import sentiment
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sentiment.train('neg.txt', 'afterclass.txt')
sentiment.save('C:\Python27\Lib\site-packages\snownlp\sentiment\sentiment.marshal')

txt = open('afterclass.txt')
text = txt.readlines();
txt.close()

print(u'读入成功')

sentences = []
senti_score = []
for content in text:
    a1 = SnowNLP(content)
    a2 = a1.sentiments
    sentences.append(content)
    senti_score.append(a2)
    # print('doing')

file = open('afterclass_score.txt','a')
for i in senti_score:
    file.write(str(i)+'\n');

