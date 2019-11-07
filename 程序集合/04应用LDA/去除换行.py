
fp = open('input3.txt','r')
fw = open('output3.txt','w')
lines = fp.readlines()
output = ''
for line in lines:
      if (len(line) == 1 or len(line) == 2):
            output = output + '\n' + line
      else:
            output = output + line.strip('\n')
      
fw.write(output)
fp.close()
fw.close()
      
