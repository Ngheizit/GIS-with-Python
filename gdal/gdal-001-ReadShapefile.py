# -*- coding: utf-8 -*-
import os
import sys
try:
    from osgeo import ogr
except:
    import ogr

EVN_PATH = os.getcwd() # 当前文件所在目录路径（相对路径）

'''
    driver: 数据驱动
        .open(<filename>, <update>)  获得数据源
            → update = 0: 只读; update = 1: 可写
'''

driver = ogr.GetDriverByName('ESRI Shapefile')
# filename = EVN_PATH + r'\china\Boundary.shp'
filename = EVN_PATH + r'\china\Cities.shp'
dataSource = driver.Open(filename, 0)
if(dataSource is None):
    sys.exit('could not open' + filename)
print(':::要素类{}加载成功。'.format(filename.split('\\')[len(filename.split('\\')) - 1]))
    

# 读取数据层
layer = dataSource.GetLayer(0)
'''
    参数默认为 0; ESRI Shapefile 均为0
'''
n = layer.GetFeatureCount()
print(':::该要素类拥有{}个要素。'.format(n))

## 读取数据范围
extent = layer.GetExtent()
print(":::该要素范围：{}".format(extent))
print("MinX: {0}\nMaxX: {1} \nMinY: {2} \nMaxY: {3}".format(extent[0], extent[1], extent[2], extent[3]))


## 遍历数据的feature
feat = layer.GetNextFeature()
print(':::数据几何信息：')
while(feat):
    # 提取feature几何信息
    geom = feat.GetGeometryRef()
    # geom.GetX() # x 坐标
    # geom.GetY() # y 坐标
    print(geom)
    feat = layer.GetNextFeature()
layer.ResetReading() # 复位

# 释放内存
dataSource.Destroy()


