import warnings
warnings.filterwarnings(action='ignore',category=UserWarning,module='gensim')
from pprint import pprint  # pretty-printer
from gensim import corpora, models, similarities

fp = open('丽江古城微博中文部分分词.txt','r')
result = open('result.txt','w')
documents = fp.readlines()
texts = [[word for word in document.strip().split()]
         for document in documents]

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
      for token in text:
            frequency[token] += 1
texts = [[token for token in text if frequency[token] > 20]
         for text in texts]
print("**************ÇåÏ´ºóµÄÎÄµµ*************")
from pprint import pprint  # pretty-printer
#pprint(texts)

dictionary = corpora.Dictionary(texts) #µÃµ½µ¥´ÊµÄID,Í³¼Æµ¥´Ê³öÏÖµÄ´ÎÊýÒÔ¼°Í³¼ÆÐÅÏ¢
print("**************´Ê´ü½á¹¹*************")
#print(dictionary)
print("**************´ÊID*************")
#pprint(dictionary.token2id)

#º¯Êýdoc2bow()¼òµ¥µØ¶ÔÃ¿¸ö²»Í¬µ¥´ÊµÄ³öÏÖ´ÎÊý½øÐÐÁË¼ÆÊý£¬²¢½«µ¥´Ê×ª»»ÎªÆä±àºÅ£¬
#È»ºóÒÔÏ¡ÊèÏòÁ¿µÄÐÎÊ½·µ»Ø½á¹û¡£
print("**************ÎÄµµÏòÁ¿*************")
corpus = [dictionary.doc2bow(text) for text in texts]
#pprint(corpus)

print("**************Ö÷Ìâ-´Ê¸ÅÂÊ·Ö²¼*************")
lda_model = models.ldamodel.LdaModel(corpus, num_topics=20, id2word=dictionary,  passes=200)#Ö÷ÌâÊý20  µü´ú´ÎÊý200
pprint(lda_model.print_topics(num_topics=20,num_words=50))
#result.write(str(each) for each in lda_model.print_topics(num_topics=50,num_words=40))
corpus_lda = lda_model[corpus]
print("**************ÎÄµµ-Ö÷Ìâ¸ÅÂÊ·Ö²¼*************")
for doc in corpus_lda:
      #print(doc)
      result.write(str(doc)+'\n')
result.close()

