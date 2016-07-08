#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import urllib.request, re, codecs

books = ['gn','ex','lv','nm','dt','js','jz','rt','1sm','2sm','1rs','2rs','1cr','2cr','ed','ne','et','job','sl','pv','ec','ct','is','jr','lm','ez','dn','os','jl','am','ob','jn','mq','na','hc','sf','ag','zc','ml','mt','mc','lc','jo','at','rm','1co','2co','gl','ef','fp','cl','1ts','2ts','1tm','2tm','tt','fm','hb','tg','1pe','2pe','1jo','2jo','3jo','jd','ap']
names = ['Gênesis','Êxodo','Levítico','Números','Deuteronômio','Josué','Juízes','Rute','1º Samuel','2º Samuel','1º Reis','2º Reis','1º Crônicas','2º Crônicas','Esdras','Neemias','Ester','Jó','Salmos','Provérbios','Eclesiastes','Cânticos','Isaías','Jeremias','Lamentações de Jeremias','Ezequiel','Daniel','Oséias','Joel','Amós','Obadias','Jonas','Miquéias','Naum','Habacuque','Sofonias','Ageu','Zacarias','Malaquias','Mateus','Marcos','Lucas','João','Atos','Romanos','1ª Coríntios','2ª Coríntios','Gálatas','Efésios','Filipenses','Colossenses','1ª Tessalonicenses','2ª Tessalonicenses','1ª Timóteo','2ª Timóteo','Tito','Filemom','Hebreus','Tiago','1ª Pedro','2ª Pedro','1ª João','2ª João','3ª João','Judas','Apocalipse']
chaps = [50,40,27,36,34,24,21,4,31,24,22,25,29,36,10,13,10,42,150,31,12,8,66,52,5,48,12,14,3,9,1,4,7,3,3,3,2,14,4,28,16,24,21,28,16,16,13,6,6,4,4,5,3,6,4,3,1,13,5,5,3,3,1,1,1,22]
verses = []

v_total = 31103
v_atual = 0

# Menu de Opções
print('Bible2SQL v1.0\nCreative Commons 3.0 BY-SA\n')
version = input('Versão:')
n = int(input('Livro inicial [0-65]:'))
m = int(input('Livro final [0-65]:'))

# Cria o arquivo 'version.sql'
file = codecs.open(version + '.sql', 'w+','utf-8-sig')

# Cria a tabela 'testament'
file.write("DROP TABLE IF EXISTS `testament`;\n")
file.write("CREATE TABLE IF NOT EXISTS `testament`(\n")
file.write("\t`id` INT NOT NULL AUTO_INCREMENT,\n")
file.write("\t`name` VARCHAR(45) NULL,\n")
file.write("\tPRIMARY KEY (`id`) )\n")
file.write("ENGINE = InnoDB;\n\n")

# Insere os valores da tabela 'testament'
file.write("INSERT INTO testament(name) VALUES ('Velho Testamento'),('Novo Testamento');\n\n")

# Cria a tabela 'books'
file.write("DROP TABLE IF EXISTS `books`;\n")
file.write("CREATE TABLE IF NOT EXISTS `books`(\n")
file.write("\t`id` INT NOT NULL AUTO_INCREMENT,\n")
file.write("\t`name` VARCHAR(45) NULL,\n")
file.write("\t`abbrev` VARCHAR(5) NULL,\n")
file.write("\t`testament` VARCHAR(5) NULL,\n")
file.write("\tPRIMARY KEY (`id`) )\n")
file.write("ENGINE = InnoDB;\n\n")

# Insere os valores da tabela 'books'
file.write("INSERT INTO books(id, name, abbrev,testament) VALUES ")
i = 0
while(i <= 65):
	if(i<39):
		testament = 1
	else:
		testament = 2
	file.write("('" + str(i+1) + "','" + names[i] + "','" + books[i] + "','" + str(testament) + "')")
	if(i < (len(books) - 1)):
		file.write(",")
	i += 1
file.write(';\n\n')

# Cria a tabela 'verses'
file.write("CREATE TABLE IF NOT EXISTS `verses`(\n")
file.write("\t`id` INT NOT NULL AUTO_INCREMENT,\n")
file.write("\t`version` VARCHAR(10) NULL,\n")
file.write("\t`testament` INT NULL,\n")
file.write("\t`book` INT NULL,\n")
file.write("\t`chapter` INT NULL,\n")
file.write("\t`verse` INT NULL,\n")
file.write("\t`text` TEXT NULL,\n")
file.write("\tPRIMARY KEY (`id`) )\n")
file.write("ENGINE = InnoDB;\n\n")

while(n <= m):
	book = books[n]
	name = names[n]
	chap = chaps[n]
	c = 1
	print('Parsing... ' + name)
	while(c <= chap):
		url = 'http://ie8.bibliaonline.com.br/' + version + '/' + book + '/' + str(c)
		regex = "<span class=\"text\">([a-zA-Z ,.:;!?\-_ÁáÉéÍíÓóÚúÂâÊêÔôçãõüà]+)<\/span>"
		page = urllib.request.urlopen(url)
		html = page.read()
		html = html.decode('utf-8')
		v = 1
		res = re.findall(regex, html)
		for t in res: 
			v_atual += 1
			status = v_atual/v_total * 100
			print("[" + version + "] " + name + ' ' + str(c) + ':' + str(v) + "..." + "%.2f" % status + "%")
			if(n<39):
				testament = 1
			else:
				testament = 2
			verses.append("('" + version + "','" + str(testament) + "','" + str(n+1) + "','" + str(c) + "','" + str(v) + "','" + t + "')")
			v += 1
		c += 1
	n += 1
print('Finished Parsing... Creating file')

i = 0

file.write("INSERT INTO verses(version,testament,book,chapter,verse,text) VALUES ")
for verse in verses:
	file.write(verse)
	if(i < (len(verses)-1)):
		file.write(',')
	i += 1
file.write(';')
file.close()
print('Done...')