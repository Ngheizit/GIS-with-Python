# -*- coding: utf-8 -*-
import os
import zipfile

# ArcGIS API for Pyhton
from arcgis.gis import GIS

###############################################################################

# 参数1： 用户名
username = "xizhewu"

# 参数2： 密码
password = "Wxz041499"

# 参数3： 矢量数据(.sho)文件路径
data_file_path = r"D:\geodata\ch_2015\ch_100w\web\TRAIN.shp"

# 参数3： 数据信息设置
properties = {
    'title': '中国主要铁路',
    'tags': '中国, 铁路, 线状要素',
    'type': 'Shapefile'
}

# 参数4： 上传至Online文件夹名
data_online_folder = "ChinaBaseData"

##############################################################################

# 登录ArcGIS Online
gis = GIS("https://www.arcgis.com", username, password)
print(':::已连接至：{}'.format(gis))


data_file_name = (data_file_path.split('\\')[len(data_file_path.split('\\')) - 1]).split('.')[0]
data_file_dir = os.path.dirname(data_file_path)


data_shapefile = [] 
for root, dirs, files in os.walk(data_file_dir):
    for file in files:
        if os.path.splitext(file)[0] == data_file_name:
            data_shapefile.append(os.path.join(root, file))
print(':::打包矢量文件：{}'.format(data_shapefile))
           
data_zipname = data_file_name + '.zip'
f = zipfile.ZipFile(data_zipname,'w',zipfile.ZIP_DEFLATED)
for file in data_shapefile:
    name = file.split('\\')[-1]
    f.write(file, name)
f.close()
print(':::Zip压缩包 "{}" 已生成'.format(data_zipname))


shp = gis.content.add(properties, data=data_zipname, folder=data_online_folder)
print(':::数据{0}已上传值ArcGIS Online账户的 "{1}" 文件夹中'.format(shp, data_online_folder))

parks_feature_layer_item = shp.publish()
print(":::已设置为公开数据：{}".format(parks_feature_layer_item))
print(":::数据共享网络路径：{}".format(parks_feature_layer_item.url))

os.remove(data_zipname) # 删除中间数据（打包Zip数据）


