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
filename = EVN_PATH + r'\china\Boundary.shp'
# filename = EVN_PATH + r'\china\Cities.shp'
dataSource = driver.Open(filename, 0)
if(dataSource is None):
    sys.exit('could not open' + filename)
print(':::要素类{}加载成功。'.format(filename.split('\\')[len(filename.split('\\')) - 1]))
# 读取数据层
layer = dataSource.GetLayer(0)


#------------------------------------------------------------------------------

# 属性过滤 Attribute filters
n = layer.GetFeatureCount()
print('属性过滤前，该要素类有 {} 个要素'.format(n))
layer.SetAttributeFilter("id = 1")
n = layer.GetFeatureCount()
print('属性过滤后，该要素类有 {} 个要素'.format(n))
# 清除属性过滤
layer.SetAttributeFilter(None)
n = layer.GetFeatureCount()
print('清除属性过滤，该要素类的要素数目恢复为{}'.format(n))

# 空间过滤 Spatial filters
layer.SetSpatialFilterRect(100000, 4000000, 1000000, 5000000)
n = layer.GetFeatureCount()
print('空间过滤后，该要素类有 {} 个要素'.format(n))
# 清除属性过滤
layer.SetSpatialFilter(None)
n = layer.GetFeatureCount()
print('清除空间过滤，该要素类的要素数目恢复为{}'.format(n))

# SQL语句过滤
'''
layer = dataSource.ExecuteSQL("select count(*) from sites where id = 1")
print(layer)


layer = dataSource.ExecuteSQL("select * from sites where id = 1 order by NAME desc")
feat = layer.GetNextFeature()
while feat:
    print(feat.GetField('NMAE'))
    feat = layer.GetNextFeature()
dataSource.ReleaseResultSet(layer)
'''





