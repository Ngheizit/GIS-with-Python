# -*- coding: utf-8 -*-
import jieba
import sys

# txt = open("丽江古城微博中文部分分词.txt", "r").read()
txt = open(sys.argv[1], "r").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(200):
    word, count = items[i]
    print("{0:<10}{1:<5}".format(word, count))
