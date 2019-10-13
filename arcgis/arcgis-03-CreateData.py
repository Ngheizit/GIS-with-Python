# -*- coding: utf-8 -*-

from arcgis.gis import GIS
import time

###############################################################################

# 参数1： 用户名
username = "xizhewu"

# 参数2： 密码
password = "Wxz041499"

##############################################################################

gis = GIS("https://www.arcgis.com", username, password)
print('已连接至：{}'.format(gis))

query = 'title: ""'
search_results = gis.content.search(query=query, max_items=100)
# print(search_results)


for data in search_results:
    print(data)
    print(data.title)
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(float(data.created / 1000))))
    print(data.tags)
    print(data.id)
    # print(data.layers[0].url)
    print('')




