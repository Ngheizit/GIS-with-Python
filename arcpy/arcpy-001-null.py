
import os
import sys
arcpy_path = [r'D:\software\ArcGIS\python 27\ArcGIS10.2\Lib\site-packages',
              r'D:\software\ArcGIS\Desktop 10.2\Desktop10.2\arcpy',
              r'D:\software\ArcGIS\Desktop 10.2\Desktop10.2\bin',
              r'D:\software\ArcGIS\Desktop 10.2\Desktop10.2\ArcToolbox\Scripts']
sys.path.extend(arcpy_path)
import arcpy
arcpy.gp.overweiteOutput = 1 # 覆盖重名文件

datatypes = ["AANP",
            "AGNP",
            "BOUA",
            "BOUL",
            "BOUP",
            "HYDA",
            "HYDL",
            "HYDP",
            "LRDL",
            "LRRL",
            "RESA",
            "RESP"]

# 设置工作空间
arcpy.env.workspace = r"D:\geodata_old\ReSortOut\wg_ChinaData100w\FramingData"

# 创建文件型数据库
# arcpy.CreateFileGDB_management(workspace2, "GDB")
gdb = r"D:\geodata\ch_100w_2015\GDB.gdb"

# 读取投影坐标数据（兰伯特等积投影）
# Beijing54 = r"Lambert_Conformal_Conic_Beijing_1954.prj"
# Xian80 = r"Lambert_Conformal_Conic_Xian_1980.prj"

CGCS2000 = r"D:\geodata\ch_100w_2015\Lambert_Conformal_Conic_CGCS_2000.prj"
coord_sys = arcpy.Describe(CGCS2000).spatialReference
print(coord_sys)

# 创建要素数据集
for fcn in datatypes:
    arcpy.CreateFeatureDataset_management(gdb, fcn, coord_sys)


# 获取分幅数据库集
filelist = os.listdir(r"D:\geodata_old\ReSortOut\wg_ChinaData100w\FramingData")
print(filelist)

# 拼接数据
for datatype in datatypes:
    In_features = []
    for name in filelist:
        In_features.append("D:\\geodata_old\\ReSortOut\\wg_ChinaData100w\\FramingData\\" + name + "\\" + datatype)
    out_feature = "D:\\geodata\\ch_100w_2015\\GDB.gdb\\" + datatype + "\\" + datatype + "_mg"
    arcpy.Merge_management(In_features, out_feature)
    print("Merge data: " + out_feature)


