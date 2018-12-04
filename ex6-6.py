import jieba
txt = open("红楼梦.txt","r",encoding='GB18030').read()
words = jieba.lcut(txt)
excludes = ['这会子','怎么样','周瑞家','贾母笑','悄悄的','贾政道','袭人道','黛玉道','林姑娘','宝钗道','少不得','宝钗笑','下回分解']
counts = {}
for word in words:
    
    if len(word) == 1 or len(word) == 2:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count = items[i]
    print('{0:<10}{1:>5}'.format(word,count))
