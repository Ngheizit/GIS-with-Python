# -*- coding: utf-8 -*-
try:
    from osgeo import ogr
except:
    import ogr


# 创建Point
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(10, 20)

# 创建Line
line = ogr.Geometry(ogr.wkbLineString)
line.AddPoint(10, 10)
line.AddPoint(20, 20)
line.SetPoint(0, 30, 40) # (10, 10) -> (30, 30)
print('线段结点数：{}'.format(line.GetPointCount()))
print('线段第{0}索引结点的X坐标：{1}\n线段第{0}索引结点的Y坐标：{2}'.
      format(0, line.GetX(), line.GetY()))

# 创建环（Ring）
ring = ogr.Geometry(ogr.wkbLinearRing)
ring.AddPoint(0, 0)
ring.AddPoint(100, 0)
ring.AddPoint(100, 100)
ring.AddPoint(0, 100)
ring.CloseRings() # or ring.AddPoint(0, 0) 闭合环路

# 创建Polygong（由环构成）
outring = ogr.Geometry(ogr.wkbLinearRing)
outring.AddPoint(0,0)
outring.AddPoint(100,0)
outring.AddPoint(100,100)
outring.AddPoint(0,100)
outring.AddPoint(0,0)
inring = ogr.Geometry(ogr.wkbLinearRing)
inring.AddPoint(25,25)
inring.AddPoint(75,25)
inring.AddPoint(75,75)
inring.AddPoint(25,75)
inring.CloseRings()
polygon = ogr.Geometry(ogr.wkbPolygon)
polygon.AddGeometry(outring)
polygon.AddGeometry(inring)
print(polygon)
print('该Polygon对象拥有环数：{}'.format(polygon.GetGeometryCount()))
outring = polygon.GetGeometryRef(0)
inring = polygon.GetGeometryRef(1)
print('该Polygon对象的环：\n{0}\n{1}'.format(outring, inring))


# 创建复合集合形状（multi geometry）
multipoint = ogr.Geometry(ogr.wkbMultiPoint)
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(10, 10)
# point.AddPoint(10, 0)
multipoint.AddGeometry(point)
point.AddPoint(20, 20)
multipoint.AddGeometry(point)
print(multipoint)


