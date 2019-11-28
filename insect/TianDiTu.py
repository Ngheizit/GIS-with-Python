# -*- coding: utf-8 -*-
import json
import requests
import csv

tk = '82336205e2fbc3838263aeb80c78112a'
key = '1'
mapBound = "116.04577,39.70307,116.77361,40.09583"
queryType = '7'

############

def CreateJSON_GeneralSearch(keyWord, level, mapBound, queryType, count, start):
    return {
        "keyWord": keyWord,
        "level": level,
        "mapBound": mapBound,
        "queryType": queryType,
        "count": count,
        "start": start
    }

count = '1'
data = {
    'postStr': str(CreateJSON_GeneralSearch(key, "20", mapBound, queryType, count, "0")),
    'type': 'query',
    'tk': tk
}
r = requests.get('http://api.tianditu.gov.cn/search', params=data)

dic = json.loads(r.text)
count = dic['count']

data = {
    'postStr': str(CreateJSON_GeneralSearch(key, "20", mapBound, queryType, count, "0")),
    'type': 'query',
    'tk': tk
}
r = requests.get('http://api.tianditu.gov.cn/search', params=data)
dic = json.loads(r.text)
pois = dic['pois']


with open('TianDiTuPOIs.csv', 'w', newline='') as csvfile:
    fieldnames = ['hotPointID', 'lon', 'lat', 'name', 'ename', 'address', 'phone', 'eaddress']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for poi in pois:
        poi['lon'] = poi['lonlat'].split(' ')[0]
        poi['lat'] = poi['lonlat'].split(' ')[1]
        del poi['lonlat']
        try:
            del poi['poiType']
            del poi['stationData']
        except:
            pass
        writer.writerow(poi)

    


