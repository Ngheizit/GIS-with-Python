# -*- coding: utf-8 -*-

from arcgis.gis import GIS

###############################################################################

# 参数1： 用户名
username = "xizhewu"

# 参数2： 密码
password = "XXX"

##############################################################################

gis = GIS("https://www.arcgis.com", username, password)
print('已连接至：{}'.format(gis))

query = 'title: "Parks" AND type: "Feature*"'
search_results = gis.content.search(query=query, max_items=10)
print(search_results)


data = search_results[0]
print(data.url)

feature_layers = data.layers
print(feature_layers)

layer = feature_layers[0]
print(layer.properties.name)

for field in layer.properties['fields']:
    print('Name: {:16s}\tType: {}'.format(field['name'], field['actualType']))


