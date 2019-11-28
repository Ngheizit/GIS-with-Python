

import arcpy
arcpy.gp.overweiteOutput = 1


shp = r'D:\geodata\ch_2015\ch_100w\BOUA_PJ.shp'

with arcpy.da.SearchCursor(shp, 'NAME') as cursor:
    for row in cursor:
        print(row)
    
