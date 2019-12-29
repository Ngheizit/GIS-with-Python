# -*- coding: utf-8 -*-

from wordcloud import WordCloud
from PIL import Image as image
import numpy as np
import jieba
import sys


def trans_CN(text):
    word_list = jieba.cut(text)
    result = ' '.join(word_list)
    return result

with open('word.txt') as fp:
    text = fp.read()
    # text = trans_CN(text)
    # print(text)
    mask = np.array(image.open('extent.png'))
    wordcloud = WordCloud(
        mask = mask,
        background_color = '#ffffff',
        collocations = False,
        font_path = r'C:\Windows\Fonts\msyh.ttc'
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()
    image_produce.save("worlcloud.png")
    