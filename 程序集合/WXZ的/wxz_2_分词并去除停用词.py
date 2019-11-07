# -*- coding: utf-8 -*-
import jieba

source = open('丽江古城微博中文部分.txt','r')
result = open('丽江古城微博中文部分分词.txt', 'w')
stopwords = {}.fromkeys([line.rstrip() for line in open('stopwords.txt')])
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
    result.write(output + '\n')
    final = []
source.close()  
result.close()
print('OK')
