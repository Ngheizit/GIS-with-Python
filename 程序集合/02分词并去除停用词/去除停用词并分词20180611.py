import jieba

source = open('丽江古城中文.txt','r')
result = open('丽江古城分词.txt', 'w')
stopwords = {}.fromkeys([line.rstrip() for line in open('stopwords.txt')])
lines = source.readlines()
final = []
for line in lines:
    line = line.rstrip('\n')
    segs = jieba.cut(line, cut_all=False)
    for seg in segs:
        # seg = seg.encode('gbk','ignore')
        if not seg in stopwords:
            if len(seg) > 1:
                final.append(seg)
    #seglist = jieba.cut(final,cut_all=False)
    output = ' '.join(final)
    #output = output.encode('gbk','ignore')
    #if output != ' ':
    result.write(output + '\n')
    #print output
    final = []
source.close()  
result.close()    
