#coding:utf-8
from jieba.analyse import *

with open('丽江古城微博中文部分分词.txt','rb') as f:
    data = f.read()

for keyword, weight in extract_tags(data, topK=50,withWeight=True):
    print('%s %s' % (keyword, weight))    
