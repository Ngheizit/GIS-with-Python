# -*- coding: utf-8 -*-
import sys
from osgeo import ogr
import os

DIR_NAME = os.getcwd() # 当前文件所在目录路径（相对路径）
ds = ogr.Open(DIR_NAME + "\\" + r"GeoData", 1)
if ds is None:
    sys.exit('Could not open floder.')


