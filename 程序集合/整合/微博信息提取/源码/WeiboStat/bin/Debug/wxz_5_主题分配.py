# -*- coding: utf-8 -*-
import sys

f = open(sys.argv[1], 'r')
w = open(sys.argv[2], 'w')
lines = f.readlines()

for line in lines:
    list = line.strip().split(',')
    maxvalue = list[1]
    maxi = 0
    for i in range(1,len(list),2):
        if list[i] > maxvalue:
            maxvalue = list[i]
            maxi = i-1
    result = list[maxi]
    result = result[2:]
    print(result)
    w.write(result + '\n')
f.close()