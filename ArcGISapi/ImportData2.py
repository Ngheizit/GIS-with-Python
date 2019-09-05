# -*- coding: utf-8 -*-
from arcgis.gis import GIS
import zipfile
import os

# ---------------------------------------------------

def getAnShapefiles(shp_dir, shp_name): 
    L=[] 
    for root, dirs, files in os.walk(shp_dir):
        for file in files:
            if os.path.splitext(file)[0] == shp_name:
                L.append(os.path.join(root, file))
    return L

def getSimpleNameFromFile(file):
    return file.split('\\')[-1].split('.')[0]

def getDirFromFile(file):
    return os.path.dirname(file)

def ShapefileToZip(shapefiles, Zipname):
    f = zipfile.ZipFile(Zipname + '.zip','w',zipfile.ZIP_DEFLATED)
    for file in shapefiles:
        name = file.split('\\')[-1]
        f.write(file, name)
    f.close()
    return Zipname + '.zip'
    
def ImportDataToOnline(data_file_location, properties):
    gis = GIS("https://www.arcgis.com", username="xizhewu", password="Wxz041499")
    shp = gis.content.add(properties, data=data_file_location)
    parks_feature_layer_item = shp.publish()
    print("→ {}".format(shp))
    print("→ {}".format(parks_feature_layer_item))
    print("→ {}".format(parks_feature_layer_item.url))
    
    

# ---------------------------------------------------
    
shp_path = r"D:\ngheizit\gis\GIS_datas\ReSortOut\全球线状水系数据100w\世界线状水系.shp"
properties = {
    'title': '全球线状水系',
    'tags': 'water, world, 100w',
    'type': 'Shapefile'
}


# ---------------------------------------------------

shp_name = getSimpleNameFromFile(shp_path) # 获取文件名（不含目录及后缀名）

shp_dir = getDirFromFile(shp_path) # 获得文件所在目录

shp_files = getAnShapefiles(shp_dir, shp_name) # 获得Shapefile文件集
print(shp_files)

shp_zip = ShapefileToZip(shp_files, shp_name) # Zip压缩文件（压缩Shapefile文件集）

ImportDataToOnline(shp_zip, properties) # 发布至Online

os.remove(shp_zip) # 删除中间数据（打包Zip数据）







