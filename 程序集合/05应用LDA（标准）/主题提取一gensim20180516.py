import warnings
warnings.filterwarnings(action='ignore',category=UserWarning,module='gensim')
from pprint import pprint  # pretty-printer
from gensim import corpora, models, similarities

fp = open('丽江古城分词2.txt','r')
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
texts = [[token for token in text if frequency[token] > 2]
         for text in texts]
print("**************清洗后的文档*************")
from pprint import pprint  # pretty-printer
#pprint(texts)

dictionary = corpora.Dictionary(texts) #得到单词的ID,统计单词出现的次数以及统计信息
print("**************词袋结构*************")
#print(dictionary)
print("**************词ID*************")
#pprint(dictionary.token2id)

#函数doc2bow()简单地对每个不同单词的出现次数进行了计数，并将单词转换为其编号，
#然后以稀疏向量的形式返回结果。
print("**************文档向量*************")
corpus = [dictionary.doc2bow(text) for text in texts]
#pprint(corpus)

print("**************主题-词概率分布*************")
lda_model = models.ldamodel.LdaModel(corpus, num_topics=10, id2word=dictionary,  passes=1000)
pprint(lda_model.print_topics(num_topics=10,num_words=50))
#result.write(str(each) for each in lda_model.print_topics(num_topics=50,num_words=40))
corpus_lda = lda_model[corpus]
print("**************文档-主题概率分布*************")
for doc in corpus_lda:
      #print(doc)
      result.write(str(doc)+'\n')
result.close()

