# -*- coding: utf-8 -*-

import sys

arcpy_path = [r'D:\software\ArcGIS\python 27\ArcGIS10.2\Lib\site-packages',
              r'D:\software\ArcGIS\Desktop 10.2\Desktop10.2\arcpy',
              r'D:\software\ArcGIS\Desktop 10.2\Desktop10.2\bin',
              r'D:\software\ArcGIS\Desktop 10.2\Desktop10.2\ArcToolbox\Scripts']

sys.path.extend(arcpy_path)

import arcpy
arcpy.gp.overweiteOutput = 1


shp = r'D:\geodata\ch_2015\ch_100w\BOUA_PJ.shp'

with arcpy.da.SearchCursor(shp, '*') as cursor:
    for row in cursor:
        for col in row:
            print(col),
        print('')
    
