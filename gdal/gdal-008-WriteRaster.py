# -*- coding: utf-8 -*-
import os, sys, numpy
try:
    from osgeo import gdal
except:
    import gdal
from osgeo.gdalconst import *

EVN_PATH = os.getcwd() # 当前文件所在目录路径（相对路径）


# GDAL 数据驱动
driver = gdal.GetDriverByName('HFA')
driver.Register()

# 打开已有栅格数据集
# filename = EVN_PATH + r'\raster\n43_35_2010lc030.tif'
filename = EVN_PATH + r'\raster\l5tm20091102b1to7c6.img'
# filename = EVN_PATH + r'\raster\l8oli20180212b1to7c7.img'

dataSource = gdal.Open(filename, GA_ReadOnly)
if dataSource is None:
    sys.exit('Could not open' + filename)
print('已打开栅格数据集：{}'.format(filename.split('\\')[len(filename.split('\\')) - 1]))


cols = dataSource.RasterXSize
rows = dataSource.RasterYSize

# 计算NDVI
band2 = dataSource.GetRasterBand(3)
band3 = dataSource.GetRasterBand(4)
data2 = band2.ReadAsArray(0, 0, cols,rows).astype(numpy.float16)
data3 = band3.ReadAsArray(0, 0, cols,rows).astype(numpy.float16)
mask = numpy.greater(data3 + data2, 0)
ndvi = numpy.choose(mask, (-99, (data3 - data2) / (data3 + data2)))
print(ndvi)

# 创建新的栅格数据集，并写入NDVI
filename = EVN_PATH + r'\raster\test2.img'
outDataset = driver.Create(filename, cols, rows, 1, GDT_Float32)
outBand = outDataset.GetRasterBand(1)
outBand.WriteArray(ndvi, 0, 0)
outBand.SetNoDataValue(-99)
ND = outBand.GetNoDataValue()
print(ND)
