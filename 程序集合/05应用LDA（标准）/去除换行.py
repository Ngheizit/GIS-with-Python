
fp = open('主题-词语.txt','r')
fw = open('主题-词语处理后.txt','w')
lines = fp.readlines()
output = ''
print(len(lines[33]))
for line in lines:
      if (len(line) == 2):
            output = output + '\n'
      else:
            output = output + line.strip('\n')
      
fw.write(output)
fp.close()
fw.close()
      
