import sys
import os

arcpy_path = [r'D:\software\ArcGIS\python 27\ArcGIS10.2\Lib\site-packages',
              r'D:\software\ArcGIS\Desktop 10.2\Desktop10.2\arcpy',
              r'D:\software\ArcGIS\Desktop 10.2\Desktop10.2\bin',
              r'D:\software\ArcGIS\Desktop 10.2\Desktop10.2\ArcToolbox\Scripts']

sys.path.extend(arcpy_path)

import arcpy
arcpy.gp.overweiteOutput = 1

def writePrj(shpPath, test):
    prj = open(shpPath.split('.')[0] + '.prj', 'w')
    prj.write(test)
    prj.close()

def CreateCGCS2000prj(shpPath):
    body = 'GEOGCS["CGCS_2000",DATUM["D_2000",SPHEROID["S_2000",6378137.0,298.2572221010041]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'
    writePrj(shpPath, body)
def CreateWGS84(shpPath):
    body = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'
    writePrj(shpPath, body)
def CreateBeijing54(shpPath):
    body = 'GEOGCS["GCS_Beijing_1954",DATUM["D_Beijing_1954",SPHEROID["Krasovsky_1940",6378245.0,298.3]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'
    writePrj(shpPath, body)
def CreateXian54(shpPath):
    body = 'GEOGCS["GCS_Xian_1980",DATUM["D_Xian_1980",SPHEROID["Xian_1980",6378140.0,298.257]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'
    writePrj(shpPath, body)
    
    
def CreatePoint(shpPath, pointList):
    point = arcpy.Point()
    pointGeoms = []
    for pt in pointList:
        point.X = pt[0]
        point.Y = pt[1]
        pointGeoms.append(arcpy.PointGeometry(point))
    arcpy.CopyFeatures_management(pointGeoms, shpPath)

ptList =[[20.000,43.000],[25.500, 45.085],[26.574, 46.025], [28.131, 48.124]]
shpPath = r'D:\geodata\test\point.shp'
CreatePoint(shpPath, ptList)
CreateCGCS2000prj(shpPath)