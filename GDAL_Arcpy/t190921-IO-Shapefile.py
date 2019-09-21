# -*- coding: utf-8 -*-

from osgeo import ogr
import os
import sys


DIR_NAME = os.getcwd() # 当前文件所在目录路径（相对路径）


fn = DIR_NAME + "\\" + r"GeoData\China\地级城市驻地.shp"

ds = ogr.Open(fn, 0) # 1. Set data source
if ds is None:
    sys.exit('Could not open {}'.format(fn))

lyr = ds.GetLayer() # 2. Get layer from data source



# 循环遍历各要素
for feat in lyr:
    pt = feat.geometry() # 要素的几何属性
    x = pt.GetX()
    y = pt.GetY()
    name = feat.GetField('NAME') # 获取指定表头的属性值
    # name = feat.GetFieldAsString('NAME') # 获取指定表头的属性值
    print("({0}, {1}) > name: {2}".format(x, y, name))

# 获取指定索引的要素
count = lyr.GetFeatureCount()
last_feature = lyr.GetFeature(count - 1)
print(last_feature.NAME)

