# -*- coding: utf-8 -*-

# ArcGIS API for Pyhton
from arcgis.gis import GIS

# Python 标准模块库
from pathlib import Path

###############################################################################

# 参数1：下载数据ID值
public_data_item_id = '18e26818769f442f975918578a6fcb97'

# 参数2：用户名
username = "xizhewu"

# 参数3： 密码
password = "xxx"

###############################################################################


# 2. 使用ArcGIS Online匿名连接下载数据
xizhewu_gis = GIS("https://www.arcgis.com", username, password)
print('已连接至：{}'.format(xizhewu_gis))

# 3. 通过ID值检索ArcGIS Online内容
data_item = xizhewu_gis.content.get(public_data_item_id)
print('已检索数据：{}'.format(data_item))

# 4. 下载
data_dir = Path('./download')
if not data_dir.exists():
    data_dir.mkdir()

data_item.download(save_path=data_dir)
print('数据 "{}" 已下载'.format(str(data_item).split('"')[1]))