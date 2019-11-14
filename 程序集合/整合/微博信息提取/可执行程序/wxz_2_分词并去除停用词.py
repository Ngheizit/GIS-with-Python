# -*- coding: utf-8 -*-
import jieba
import sys

# source = open('丽江古城微博中文部分.txt','r')
source = open(sys.argv[1],'r')

# stopwords = {}.fromkeys([line.rstrip() for line in open('stopwords2.txt', encoding='UTF-8')])
stopwords = {}.fromkeys([line.rstrip() for line in open(sys.argv[2], encoding='UTF-8')])

# result = open('丽江古城微博中文部分分词.txt', 'w')
result = open(sys.argv[3], 'w')

lines = source.readlines()
final = []
for line in lines:
    line = line.rstrip('\n')
    segs = jieba.cut(line, cut_all=False)
    for seg in segs:
        if not seg in stopwords:
            if len(seg) > 1:
                final.append(seg)
    output = ' '.join(final)
    print(output + '\n')
    result.write(output + '\n')
    final = []
source.close()  
result.close()
print('OK')
