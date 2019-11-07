import xlrd
import re

pattern = re.compile('[\x80-\xff]+')


source = xlrd.open_workbook('丽江古城微博文本部分.xlsx')
source_table = source.sheet_by_name('Sheet1')
rows = source_table.nrows
w = open('丽江古城微博中文部分.txt','w')

for row in range(1,rows):
    #fid = int(source_table.cell_value(row,0))
    #w.write(str(fid)+',')
    text = source_table.cell_value(row,6)
    text = text.encode('gbk','ignore')
    ch = re.findall(pattern,text)
    for each in ch:
        w.write(each)
        print(each)
    w.write('\n')

w.close()
    
    
    
