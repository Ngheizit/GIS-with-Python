# -*- coding: utf-8 -*-
f = open("txt.txt")
line = f.readline()
i = 0
while line:
    i = line.find('.')
    if not i == -1:
        icon = line[line.find('-') + 1:line.find(':')]
        print('"{}",'.format(icon))
    line = f.readline()
f.close()
