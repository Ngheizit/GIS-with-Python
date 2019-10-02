# -*- coding: utf-8 -*-
try:
    from osgeo import ogr
except:
    import ogr
    
line1 = ogr.Geometry(ogr.wkbLineString)
line1.AddPoint(10, 10)
line1.AddPoint(20, 20)
print('line1：{}'.format(line1))

line2 = ogr.Geometry(ogr.wkbLineString)
line2.AddPoint(20, 10)
line2.AddPoint(10, 20)
print('line2：{}'.format(line2))

# 判断两个要素是否相交 Intersect
print('line1 和line2 是否相交：{}'.format(line1.Intersect(line2)))

# 判断两要素是否不相交 Disjoint
print('line1 和line2 是否不相交：{}'.format(line1.Disjoint(line2)))

line2.SetPoint(1, 30, 20)
print('line2：{}'.format(line2))
print('line1 和line2 是否相交：{}'.format(line1.Intersect(line2)))
print('line1 和line2 是否不相交：{}'.format(line1.Disjoint(line2)))
line2.SetPoint(1, 10, 20)


# 判断是否相邻 Touch
print('line1：{}'.format(line1))
print('line2：{}'.format(line2))
print('line1 和line2 是否相邻：{}'.format(line1.Touches(line2)))
line2.SetPoint(1, 15, 15)
print('line2：{}'.format(line2))
print('line1 和line2 是否相邻：{}'.format(line1.Touches(line2)))

# 判断是否穿越 Crosses
print('line1 和line2 是否穿越：{}'.format(line1.Crosses(line2)))
line2.SetPoint(1, 10, 20)
print('line2：{}'.format(line2))
print('line1 和line2 是否穿越：{}'.format(line1.Crosses(line2)))

# 判断是否包含（一要素完全被另一要素圈起来） Within
ring1 = ogr.Geometry(ogr.wkbLinearRing)
ring1.AddPoint(0,0)
ring1.AddPoint(100,0)
ring1.AddPoint(100,100)
ring1.AddPoint(0,100)
ring1.AddPoint(0,0)
polygon1 = ogr.Geometry(ogr.wkbPolygon)
polygon1.AddGeometry(ring1)
ring2 = ogr.Geometry(ogr.wkbLinearRing)
ring2.AddPoint(25,25)
ring2.AddPoint(75,25)
ring2.AddPoint(75,75)
ring2.AddPoint(25,75)
ring2.CloseRings()
polygon2 = ogr.Geometry(ogr.wkbPolygon)
polygon2.AddGeometry(ring2)
print('polygon1：{}'.format(polygon1))
print('polygon2：{}'.format(polygon2))
print('polygon1 是否被包含在 polygon2：{}'.format(polygon1.Within(polygon2)))
print('polygon2 是否被包含在 polygon1：{}'.format(polygon2.Within(polygon1)))
# Contains 与Within相反
print('polygon1 是否不被包含在 polygon2：{}'.format(polygon1.Contains(polygon2)))
print('polygon2 是否不被包含在 polygon1：{}'.format(polygon2.Contains(polygon1)))

# 判断两多边形是否重叠 Overlaps
print('polygon2 是否与 polygon1 重叠：{}'.format(polygon2.Overlaps(polygon1)))
ring3 = ogr.Geometry(ogr.wkbLinearRing)
ring3.AddPoint(0,0)
ring3.AddPoint(100,0)
ring3.AddPoint(100,100)
ring3.AddPoint(0,100)
ring3.AddPoint(0,0)
polygon3 = ogr.Geometry(ogr.wkbPolygon)
polygon3.AddGeometry(ring3)
print('polygon3：{}'.format(polygon3))
print('polygon1 是否与 polygon3 重叠：{}'.format(polygon1.Overlaps(polygon3)))


