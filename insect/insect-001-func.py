# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys

url = 'https://ngheizit.fun'

# 网页提取框架
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        return r.text
    except:
        sys.exit('{}网页提取失败'.format(url))
        return None

r = getHTMLText(url)
soup = BeautifulSoup(r, 'html.parser')
tag = soup.style
print(tag.string)