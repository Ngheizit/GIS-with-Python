
f = open('丽江古城分词.txt','r')
w = open('丽江古城分词2.txt','w')
lines = f.readlines()
for line in lines:
      if len(line.strip()) > 0:
            w.write(line)

f.close()
w.close()
            
