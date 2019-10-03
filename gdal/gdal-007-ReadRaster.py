# -*- coding: utf-8 -*-
import os, sys, utils, numpy
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

# 读取栅格数据集的x方向像素数，y方向像素数和波段数
cols = dataSource.RasterXSize
rows = dataSource.RasterYSize
bands = dataSource.RasterCount
print('该栅格数据集x轴方向像素数为{0}，y轴像素数为{1}，波段数为{2}'.format(cols, rows, bands))

# 读取地理坐标参考信息
geotransform = dataSource.GetGeoTransform()
originX = geotransform[0] # 左上角x坐标
originY = geotransform[3] # 左上角y坐标
pixelWidth = geotransform[1] # 东西向像素分辨率
pixelHeight = geotransform[5] # 南北向像素分辨率
print('该栅格数据集：\n    左上角x坐标：{0}\n    左上角y坐标：{1}\n    东西向像素分辨率：{2}\n    南北向像素分辨率：{3}\n'
      .format(originX, originY, pixelWidth, pixelHeight))
# GeoTransform[0] /* top left x 左上角x坐标*/
# GeoTransform[1] /* w--e pixel resolution 东西方向上的像素分辨率*/
# GeoTransform[2] /* rotation, 0 if image is "north up" 如果北边朝上，地图的旋转角度*/
# GeoTransform[3] /* top left y 左上角y坐标*/
# GeoTransform[4] /* rotation, 0 if image is "north up" 如果北边朝上，地图的旋转角度*/
# GeoTransform[5] /* n-s pixel resolution 南北方向上的像素分辨率*/

# 计算某一坐标对应像素的相对位置（相对于左上角）
x = 769715
y = 2481094
xOffset = int((x - originX) / pixelWidth)
yOffset = int((y - originY) / pixelHeight)
print('地理坐标({0}, {1})相对栅格数据像素的位置为({2}, {3})'.format(x, y, xOffset, yOffset))

# 读取某一像素点的值
band = dataSource.GetRasterBand(1) # 获取某一波段
data = band.ReadAsArray(xOffset, yOffset, 1, 1)
print(data)
# 使用utils包
'''
blockSize = utils.GetBlockSize(band)
xBlockSize = blockSize[0]
yBlockSize = blockSize[1]
'''


# 栅格矩阵
data = band.ReadAsArray(391, 1000, 10, 10)
'''
for i in range(0, rows - 1):
    for j in range(0, cols - 1):
            print(data[i][j], end='')
    print('')
'''
# data = data.astype(numpy.float) # 举证类型转为浮点型
print(data)

# 矩阵淹没
data = numpy.greater(data, 0)
print(data)

# 统计大于零的像素个数
print(numpy.sum(data))
