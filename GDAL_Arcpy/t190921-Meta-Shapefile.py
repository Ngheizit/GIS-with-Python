# -*- coding: utf-8 -*-

from osgeo import ogr
import os
import sys

DIR_NAME = os.getcwd() # 当前文件所在目录路径（相对路径）


fn_point = DIR_NAME + "\\" + r"GeoData\China\地级城市驻地.shp"
fn_line = DIR_NAME + "\\" + r"GeoData\China\主要河流.shp"
fn_poly = DIR_NAME + "\\" + r"GeoData\China\省级行政区.shp"

ds = ogr.Open(fn_point)
lyr = ds.GetLayer(0)

extent = lyr.GetExtent() # (mix_x, max_x, min_y, max_y)
print(extent)

print(lyr.GetGeomType() == ogr.wkbPoint) # False

feat = lyr.GetFeature(0)
print(feat.geometry().GetGeometryName()) # POINT, LINESTRING, POLYGON

print(lyr.GetSpatialRef()) # 获取空间参考



# 遍历字段信息（字段名称 + 字段类型）
for field in lyr.schema:
    print("{} > {}".format(field.name, field.GetTypeName()))