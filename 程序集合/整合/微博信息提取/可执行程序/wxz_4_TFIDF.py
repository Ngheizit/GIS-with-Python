# -*- coding: utf-8 -*-
from jieba.analyse import *
import sys

with open(sys.argv[1],'rb') as f:
    data = f.read()

for keyword, weight in extract_tags(data, topK=20,withWeight=True):
    print('%s %s' % (keyword, weight))    
