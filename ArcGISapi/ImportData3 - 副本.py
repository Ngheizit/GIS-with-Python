# -*- coding: utf-8 -*-
import tkinter
from tkinter import messagebox

# --------------------------------------------------------------

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
    
def ImportDataToOnline(data_file_location, properties, Username, Password):
    gis = GIS("https://www.arcgis.com", username=Username, password=Password)
    shp = gis.content.add(properties, data=data_file_location)
    feature_layer_item = shp.publish()
    return feature_layer_item.url
    

# ---------------------------------------------------
'''
shp_path = r"D:\ngheizit\gis\GIS_datas\ReSortOut\全球线状水系数据100w\世界线状水系.shp"
properties = {
    'title': '全球线状水系',
    'tags': 'water, world, 100w',
    'type': 'Shapefile'
}
'''

# ---------------------------------------------------



# --------------------------------------------------------------




top = tkinter.Tk()

entry_username = tkinter.Entry(top, bd =5, width = 4)
entry_username.pack(side = tkinter.LEFT)

entry_password = tkinter.Entry(top, bd =5, width = 4)
entry_password.pack(side = tkinter.LEFT)

entry_title = tkinter.Entry(top, bd =5, width = 20)
entry_title.pack(side = tkinter.LEFT)

entry_tags = tkinter.Entry(top, bd =5, width = 20)
entry_tags.pack(side = tkinter.LEFT)

entry_type = tkinter.Entry(top, bd =5, width = 20)
entry_type.pack(side = tkinter.LEFT)

entry_shppath = tkinter.Entry(top, bd =5, width = 80)
entry_shppath.pack(side = tkinter.LEFT)

def Upload():
    try:
        shp_path = entry_shppath.get()
        properties = {
            'title': entry_title.get(),
            'tags': entry_tags.get(),
            'type': entry_type.get()
        }
        shp_name = getSimpleNameFromFile(shp_path) # 获取文件名（不含目录及后缀名）
        shp_dir = getDirFromFile(shp_path) # 获得文件所在目录
        shp_files = getAnShapefiles(shp_dir, shp_name) # 获得Shapefile文件集
        shp_zip = ShapefileToZip(shp_files, shp_name) # Zip压缩文件（压缩Shapefile文件集）
        report = ImportDataToOnline(shp_zip, properties, entry_username.get(), entry_password.get()) # 发布至Online
        os.remove(shp_zip) # 删除中间数据（打包Zip数据）
        messagebox.showinfo("Successful.", report)
    except:
        messagebox.showinfo("Failed", "try to check and redo.")

btn_run = tkinter.Button(top, text="Upload", command=Upload, activebackground="#000", activeforeground="#fff")
btn_run.pack()

top.mainloop()