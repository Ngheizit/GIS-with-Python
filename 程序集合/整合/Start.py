# -*- coding: utf-8 -*-

import tkinter as tk
import xlrd
import re
import jieba

def hit_me():
    print('hello world')
    
def btnClick_CatchCN(): # 提取中文
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
    tk.messagebox.showinfo('提示','提取中文成功，已在当前文件目录下生成或更新【丽江古城微博中文部分.txt】文件')

def btnClick_CutWordAndDeleteSomeWord(): # 分词并去除停用词
    source = open('丽江古城微博中文部分.txt','r')
    result = open('丽江古城微博中文部分分词.txt', 'w')
    stopwords = {}.fromkeys([line.rstrip() for line in open('stopwords.txt', encoding='UTF-8')])
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
    tk.messagebox.showinfo('提示','分词并去除停用词成功，已在当前文件目录下生成或更新【丽江古城微博中文部分分词.txt】文件')






window = tk.Tk()
window.title('程序整合')
window.geometry('400x300')

   

# -----------这里是窗口的内容-----------



fm1 = tk.Frame()
fm1.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
fm2 = tk.Frame()
tk.Canvas(fm2).pack(side=tk.LEFT)
fm2.pack(side=tk.LEFT, padx=10)

def CreateButton(name, func):
    tk.Button(fm1, 
              text=name,  # 显示在按钮上的文字
              width=15, height=2,
              command=func  # 点击按钮式执行的命令
    ).pack()  
    
CreateButton('提取中文', btnClick_CatchCN)
CreateButton('分词并去除停用词', btnClick_CutWordAndDeleteSomeWord)
CreateButton('按钮3', hit_me)
CreateButton('按钮4', hit_me)
CreateButton('按钮5', hit_me)
CreateButton('按钮6', hit_me)



# -------------------------------------

window.mainloop()