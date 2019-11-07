# -*- coding: utf-8 -*-

import xlrd
import re

# pattern = re.compile('[\x80-\xff]+')
pattern = re.compile('[\u4e00-\u9fa5]+')


source = xlrd.open_workbook('丽江古城微博文本部分.xlsx')
source_table = source.sheet_by_name('Sheet1')
rows = source_table.nrows
w = open('丽江古城微博中文部分.txt','w')

for row in range(1,rows):
    text = source_table.cell_value(row,6)
    # text = text.encode('gbk','ignore')
    ch = re.findall(pattern,text)
    print(ch)
    for each in ch:
        w.write(each)
    w.write('\n')

w.close()
print('OK')