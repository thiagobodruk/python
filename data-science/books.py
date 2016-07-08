#!/usr/bin/python
# -*- encoding: utf-8 -*-

books = ['gn','ex','lv','nm','dt','js','jz','rt','1sm','2sm','1rs','2rs','1cr','2cr','ed','ne','et','jó','sl','pv','ec','ct','is','jr','lm','ez','dn','os','jl','am','ob','jn','mq','na','hc','sf','ag','zc','ml','mt','mc','lc','jo','at','rm','1co','2co','gl','ef','fp','cl','1ts','2ts','1tm','2tm','tt','fm','hb','tg','1pe','2pe','1jo','2jo','3jo','jd','ap']
names = ['Gênesis','Êxodo','Levítico','Números','Deuteronômio','Josué','Juízes','Rute','1º Samuel','2º Samuel','1º Reis','2º Reis','1º Crônicas','2º Crônicas','Esdras','Neemias','Ester','Jó','Salmos','Provérbios','Eclesiastes','Cânticos','Isaías','Jeremias','Lamentações de Jeremias','Ezequiel','Daniel','Oséias','Joel','Amós','Obadias','Jonas','Miquéias','Naum','Habacuque','Sofonias','Ageu','Zacarias','Malaquias','Mateus','Marcos','Lucas','João','Atos','Romanos','1ª Coríntios','2ª Coríntios','Gálatas','Efésios','Filipenses','Colossenses','1ª Tessalonicenses','2ª Tessalonicenses','1ª Timóteo','2ª Timóteo','Tito','Filemom','Hebreus','Tiago','1ª Pedro','2ª Pedro','1ª João','2ª João','3ª João','Judas','Apocalipse']
chaps = [50,40,27,36,34,24,21,4,31,24,22,25,29,36,10,13,10,42,150,31,12,8,66,52,5,48,12,14,3,9,1,4,7,3,3,3,2,14,4,28,16,24,21,28,16,16,13,6,6,4,4,5,3,6,4,3,1,13,5,5,3,3,1,1,1,22]

bible = []
for n in range(66):
    bible.append((books[n], names[n], chaps[n]))

print(bible)
