# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# import tkinter
from tkinter import messagebox, Tk, Entry, LEFT, Button

from arcgis.gis import GIS
from zipfile import ZipFile, ZIP_DEFLATED
from os import remove
from os.path import splitext, join, dirname
from os import walk

# ---------------------------------------------------

# 获得代表一份矢量数据的（所有）文件集，以列表形式返回
def GetAnShapefiles(shp_dir, shp_name):  # 参数1：矢量数据所在的目录位置；参数2：矢量数据的（纯）名称
    L=[]
    for root, dirs, files in walk(shp_dir):
        for file in files:
            if splitext(file)[0] == shp_name:
                L.append(join(root, file))
    return L

# 获得文件名（不含目录及后缀名）
def GetSimpleNameFromFile(file):
    return file.split('\\')[-1].split('.')[0]

# 获得文件所在位置
def GetDirFromFile(file):
    return dirname(file)

# 将矢量数据文件集打包压缩成Zip格式的压缩包
def ShapefileToZip(shapefiles, Zipname):
    f = ZipFile(Zipname + '.zip','w',ZIP_DEFLATED)
    for file in shapefiles:
        name = file.split('\\')[-1]
        f.write(file, name)
    f.close()
    return Zipname + '.zip'

# 将装载矢量数据的压缩包上传到指定ArcGIS Online账户
def ImportDataToOnline(data_file_location, properties, Username, Password):
    gis = GIS("https://www.arcgis.com", username=Username, password=Password)
    shp = gis.content.add(properties, data=data_file_location)
    feature_layer_item = shp.publish()
    return feature_layer_item.url

# ---------------------------------------------------

# 界面设计
top = Tk()
entry_username = Entry(top, bd =5, width = 4) # 输入：用户名
entry_username.pack(side = LEFT)
entry_password = Entry(top, bd =5, width = 4) # 输入：密码
entry_password.pack(side = LEFT)
entry_title = Entry(top, bd =5, width = 20) # 输入：名称
entry_title.pack(side = LEFT)
entry_tags = Entry(top, bd =5, width = 20) # 输入：关键词（逗号,分隔）
entry_tags.pack(side = LEFT)
entry_type = Entry(top, bd =5, width = 20) # 输入：类型 Shapeflie
entry_type.pack(side = LEFT)
entry_shppath = Entry(top, bd =5, width = 80) # 输入：文件绝对路径
entry_shppath.pack(side = LEFT)    

def Upload():
    try:
        shp_path = entry_shppath.get()
        properties = {
            'title': entry_title.get(),
            'tags': entry_tags.get(),
            'type': entry_type.get()
        }
        shp_name = GetSimpleNameFromFile(shp_path) # 获取文件名（不含目录及后缀名）
        shp_dir = GetDirFromFile(shp_path) # 获得文件所在目录
        shp_files = GetAnShapefiles(shp_dir, shp_name) # 获得Shapefile文件集
        shp_zip = ShapefileToZip(shp_files, shp_name) # Zip压缩文件（压缩Shapefile文件集）
        report = ImportDataToOnline(shp_zip, properties, entry_username.get(), entry_password.get()) # 发布至Online
        remove(shp_zip) # 删除中间数据（打包Zip数据）
        messagebox.showinfo("Successful.", report)
    except:
        messagebox.showinfo("Failed", "try to check and redo.")

btn_run = Button(top, text="Upload", command=Upload, activebackground="#000", activeforeground="#fff")
btn_run.pack()

top.mainloop()
