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
filename = EVN_PATH + r'\temp\create.shp'
# filename = 'create.shp'

# 删除Shapefile文件
driver.DeleteDataSource(filename)

# 创建Shapefile文件
dataSource = driver.CreateDataSource(filename)
print("数据{}已创建".format(filename))
layer = dataSource.CreateLayer('create', geom_type=ogr.wkbPoint)



# 新建字段
fieldDefn = ogr.FieldDefn('id', ogr.OFTString) # 字段名 + 字段类型
fieldDefn.SetWidth(4) # 字段宽度
layer.CreateField(fieldDefn)
print("字段'id'已创建")

# 创建要素
featureDefn = layer.GetLayerDefn()
feature = ogr.Feature(featureDefn)
wkt = "POINT(%f %f)" %  (1 , 2)
point = point = ogr.CreateGeometryFromWkt(wkt)
feature.SetGeometry(point)
feature.SetField('id', 23)
layer.CreateFeature(feature)
print("要素{}已创建".format(feature))

# 释放内存
dataSource.Destroy()

