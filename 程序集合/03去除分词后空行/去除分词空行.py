
f = open('�����ųǷִ�.txt','r')
w = open('�����ųǷִ�2.txt','w')
lines = f.readlines()
for line in lines:
      if len(line.strip()) > 0:
            w.write(line)

f.close()
w.close()
            
