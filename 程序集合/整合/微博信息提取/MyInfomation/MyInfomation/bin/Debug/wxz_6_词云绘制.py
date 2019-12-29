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

with open(sys.argv[1]) as fp:
    text = fp.read()
    # text = trans_CN(text)
    # print(text)
    mask = np.array(image.open(sys.argv[2]))
    wordcloud = WordCloud(
        mask = mask,
        collocations = False,
        background_color='white',
        font_path = r'C:\Windows\Fonts\msyh.ttc'
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()
    image_produce.save("worlcloud.png")
    