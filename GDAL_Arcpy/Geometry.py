# -*- coding: utf-8 -*-

from osgeo import ogr
# import os

# DIRNAME = os.getcwd() # 当前文件所在目录路径


# ------------------------------------------

def wxz_GetLayerFromShapefile(filename):
    ds = ogr.Open(filename, 0)
    return ds.GetLayer()

# ------------------------------------------


# fn = DIRNAME + "\\" + r"GeoData\China\地级城市驻地.shp"
fn = r"D:\xizhe\github_local\PythonLearning\GDAL_Arcpy\GeoData\China\地级城市驻地.shp"

lyr = wxz_GetLayerFromShapefile(fn)

i = 0
for feat in lyr:
    pt = feat.geometry()
    x = pt.GetX()
    y = pt.GetY()
    name = feat.GetField('NAME')
    print("({0}, {1}, {2})".format(x, y, name))


