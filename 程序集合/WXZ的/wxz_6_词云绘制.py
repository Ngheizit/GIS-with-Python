# -*- coding: utf-8 -*-

from wordcloud import WordCloud
from PIL import Image as image
import numpy as np
import jieba


def trans_CN(text):
    word_list = jieba.cut(text)
    result = ' '.join(word_list)
    return result

with open('丽江古城微博中文部分分词.txt') as fp:
    text = fp.read()
    # text = trans_CN(text)
    # print(text)
    mask = np.array(image.open('LOVE.jpg'))
    wordcloud = WordCloud(
        mask = mask,
        font_path = r'C:\Windows\Fonts\msyh.ttc'
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()
    