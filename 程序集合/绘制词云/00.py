# -*- coding: utf-8 -*-
#绘制词云
from wordcloud import WordCloud
from PIL import Image 
import numpy as np
import re
import matplotlib.pyplot as plt
file=open('test1.txt','rb')
text=file.read()

import chardet
encode_type = chardet.detect(text)
text = text.decode(encode_type['encoding'])

file.close()
#print(text)
words=text.split()  #将字符串打断成单词
words1=[word.lower() for word in words]  #大写转小写
words2=[re.sub("[,'.:?;]",'',word) for word in words1]#去掉标点符号
words_index=set(words)  #去重复
dic={index:words2.count(index) for index in words_index} #统计词频
graph=np.array(Image.open('LOVE.jpg'))#轮廓图片读成像素矩阵
wc=WordCloud(background_color='White',mask=graph)#设置词云背景颜色及形状
wc.generate_from_frequencies(dic)#读进词频数据
#展示图片
plt.imshow(wc)
plt.axis("off")#去除坐标轴
plt.show()

