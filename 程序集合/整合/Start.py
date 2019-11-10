# -*- coding: utf-8 -*-

import tkinter as tk
import xlrd
import re
import jieba
import warnings
warnings.filterwarnings(action='ignore',category=UserWarning,module='gensim')
from pprint import pprint  # pretty-printer
from gensim import corpora, models, similarities
from collections import defaultdict
from wordcloud import WordCloud
from PIL import Image as image
import numpy as np
from jieba.analyse import *

#-------------------------------参数设置---------------------------------------

XLSX = '丽江古城微博文本部分.xlsx' # 初始Excel数据

LDA_FOREACHS = 20 # LDA迭代次数
NUM_TOPICS = 20 # LDA num_topics 参数
NUM_WORDS = 50 # LDA num_words 参数

#-----------------------------------------------------------------------------

window = tk.Tk()
window.title('程序整合')
window.geometry('700x330')

fm2 = tk.Frame()
tbx = tk.Text(
        fm2
    )
    
def btnClick_CatchCN(): # 提取中文
    tbx.delete(0.0, tk.END)
    pattern = re.compile('[\u4e00-\u9fa5]+')
    source = xlrd.open_workbook(XLSX)
    source_table = source.sheet_by_name('Sheet1')
    rows = source_table.nrows
    w = open('结果_提取中文.txt','w')
    for row in range(1,rows):
        text = source_table.cell_value(row,6)
        # text = text.encode('gbk','ignore')
        ch = re.findall(pattern,text)
        print(ch)
        for each in ch:
            w.write(each)
            tbx.insert("end", each)
        tbx.insert("end", "\n")
        w.write('\n')
    w.close()
    tk.messagebox.showinfo('提示','提取中文成功，已在当前文件目录下生成或更新【结果_提取中文.txt】文件')

def btnClick_CutWordAndDeleteSomeWord(): # 分词并去除停用词
    tbx.delete(0.0, tk.END)
    source = open('结果_提取中文.txt','r')
    result = open('结果_分词并去除停用词.txt', 'w')
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
        tbx.insert("end", output + '\n')
        result.write(output + '\n')
        final = []
    source.close()  
    result.close()
    print('OK')
    tk.messagebox.showinfo('提示','分词并去除停用词成功，已在当前文件目录下生成或更新【结果_分词并去除停用词.txt】文件')


def btnClick_LDA():
    tbx.delete(0.0, tk.END)
    fp = open('结果_分词并去除停用词.txt','r')
    result = open('结果_LDA.txt','w')
    documents = fp.readlines()
    texts = [[word for word in document.strip().split()]
         for document in documents]
    # remove words that appear only once
    frequency = defaultdict(int)
    for text in texts:
          for token in text:
                frequency[token] += 1
    texts = [[token for token in text if frequency[token] > 20]
             for text in texts]
    print("**************清洗后的文档*************")
    # pprint(texts)
    
    dictionary = corpora.Dictionary(texts) # 得到单词的ID，统计单词出现的次数以及统计信息
    print("**************词袋结构*************")
    # print(dictionary)
    print("**************词ID*************")
    # pprint(dictionary.token2id)
    
    # 函数doc2bow() 简单地对每个不同单词的出现次数进行了计数，并将单词转换为其编号
    # 然后以稀疏向量的形式返回结果
    print("**************文档向量*************")
    corpus = [dictionary.doc2bow(text) for text in texts]
    # pprint(corpus)
    
    print("**************主题-词频率分布*************")
    lda_model = models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary,  passes=LDA_FOREACHS)#Ö÷ÌâÊý20  µü´ú´ÎÊý200
    pprint(lda_model.print_topics(num_topics=NUM_TOPICS,num_words=NUM_WORDS))
    # result.write(str(each) for each in lda_model.print_topics(num_topics=50,num_words=40))
    corpus_lda = lda_model[corpus]
    print("**************文档-主题频率分布*************")
    for doc in corpus_lda:
          # print(doc)
          result.write(str(doc)+'\n')
          tbx.insert("end", str(doc) + '\n')
    result.close()
    tk.messagebox.showinfo('提示','应用IDA成功，已在当前文件目录下生成或更新【结果_LDA.txt】文件')

def btnClick_TitleSata():
    tbx.delete(0.0, tk.END)
    f = open('结果_LDA.txt', 'r')
    w = open('结果_主题匹配.txt','w')
    lines = f.readlines()
    
    for line in lines:
            list = line.strip().split(',')
            maxvalue = list[1]
            maxi = 0
            for i in range(1,len(list),2):
                    if list[i] > maxvalue:
                            maxvalue = list[i]
                            maxi = i-1    
            #print(list[maxi])
            result = list[maxi]
            result = result[2:]
            w.write(result + '\n')
            tbx.insert("end", result + '\n')
    f.close()
    tk.messagebox.showinfo('提示','主题匹配成功，已在当前文件目录下生成或更新【结果_主题匹配.txt】文件')

def btnClick_DrawWordCloud():
    with open('结果_分词并去除停用词.txt') as fp:
        text = fp.read()
        mask = np.array(image.open('LOVE.jpg'))
        wordcloud = WordCloud(
            mask = mask,
            font_path = r'C:\Windows\Fonts\msyh.ttc'
        ).generate(text)
        image_produce = wordcloud.to_image()
        image_produce.show()

def btnClick_TFIDF():
    tbx.delete(0.0, tk.END)
    with open('结果_分词并去除停用词.txt','rb') as f:
        data = f.read()
    for keyword, weight in extract_tags(data, topK=20,withWeight=True):
        print('%s %s' % (keyword, weight))  
        tbx.insert("end", '%s %s' % (keyword, weight) + '\n')
    tk.messagebox.showinfo('提示','TFIDF成功，结果已输出至文本框')

def btnClick_WordFre():
    tbx.delete(0.0, tk.END)
    txt = open("结果_分词并去除停用词.txt", "r").read()
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
        tbx.insert("end", "{0:<10}{1:<5}".format(word, count) + '\n')
    tk.messagebox.showinfo('提示','词频计算成功，结果已输出至文本框')



   

# -----------这里是窗口的内容-----------



fm1 = tk.Frame()
fm1.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
tbx.pack(side=tk.LEFT)
fm2.pack(side=tk.LEFT, padx=10)

def CreateButton(name, func):
    tk.Button(fm1, 
              text=name,  # 显示在按钮上的文字
              width=15, height=2,
              command=func  # 点击按钮式执行的命令
    ).pack()  
    
CreateButton('提取中文', btnClick_CatchCN)
CreateButton('分词并去除停用词', btnClick_CutWordAndDeleteSomeWord)
CreateButton('应用IDA', btnClick_LDA)
CreateButton('主题统计', btnClick_TitleSata)
CreateButton('绘制词云', btnClick_DrawWordCloud)
CreateButton('TFIDF', btnClick_TFIDF)
CreateButton('词频', btnClick_WordFre)



# -------------------------------------

window.mainloop()