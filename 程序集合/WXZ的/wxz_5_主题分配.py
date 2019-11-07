# -*- coding: utf-8 -*-

f = open('result.txt', 'r')
w = open('doc-topic.txt','w')
lines = f.readlines()

for line in lines:
        list = line.strip().split(',')
        maxvalue = list[1]
        maxi = 0
        for i in range(1,len(list),2):
                if list[i] > maxvalue:
                        maxvalue = list[i]
                        maxi = i-1    
        #print(list[maxi])
        w.write(list[maxi]+'\n')
f.close()