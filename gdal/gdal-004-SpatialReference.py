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

# 读取空间参考
sptialRef = layer.GetSpatialRef()
print(':::该要素类的空间参考：\n{}'.format(sptialRef))


# 创建复合集合形状（multi geometry）
multipoint = ogr.Geometry(ogr.wkbMultiPoint)
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(10, 10)
# point.AddPoint(10, 0)
multipoint.AddGeometry(point)
point.AddPoint(20, 20)
multipoint.AddGeometry(point)
print(':::{}'.format(multipoint))

print('该geom的空间参考{}'.format(multipoint.GetSpatialReference()))
