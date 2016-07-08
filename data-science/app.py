#!/usr/bin/python
import matplotlib.pyplot as plt
import codecs, re, json

books = ['gn','ex','lv','nm','dt','js','jz','rt','1sm','2sm','1rs','2rs','1cr','2cr','ed','ne','et','job','sl','pv','ec','ct','is','jr','lm','ez','dn','os','jl','am','ob','jn','mq','na','hc','sf','ag','zc','ml','mt','mc','lc','jo','at','rm','1co','2co','gl','ef','fp','cl','1ts','2ts','1tm','2tm','tt','fm','hb','tg','1pe','2pe','1jo','2jo','3jo','jd','ap']
text = json.loads(codecs.open('acf.json', 'r+', 'utf-8-sig').read())

res = {}
words = input('Keyword: ').split(' ')
for word in words:
    res[word] = []

for book in text:
    for word in words:
        rgx = '%s' % (word)
        res[word].append(len(re.findall(rgx, str(book))))

index =[]
for i in range(1,67):
    index.append(i)

plt.grid(True)
plt.title('Palavras por Livro')
plt.xlabel('livros')
plt.ylabel('ocorrências')
plt.xticks(index, books, rotation="vertical")

times = {}

for word in words:
    times[word] = int(sum(res[word]))
    plt.plot(index, res[word], label='%s (%i)' % (word,times[word]))

print('\nBOOKS')
print(res)
print('\nOCCURRENCES')
print(times)

plt.legend()
plt.show()