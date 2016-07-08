#!/usr/bin/python
import codecs, json


class Parser:

    def __init__(self, versions):
        for version in versions:
            self.load(version)

    def load(self, version):
        file = json.loads(codecs.open('json/'+version+'.json','r','utf-8-sig').read())
        bible = []
        for book in file:
            #print(book['book'], book['abbrev'])
            b_list = []
            for chapters in book['chapters']:
                c_list = []
                for c, verses in chapters.items():
                    #print('\tChapter',c)
                    verses = {int(v):str(text) for v, text in verses.items()}
                    for v, text in verses.items():
                        #print('\t\t', v, text)
                        c_list.append(text)
                b_list.append(c_list)
            bible.append(b_list)
        j = json.dumps(bible, ensure_ascii=False)
        self.save(version, j)

    def save(self, name, content):
        try:
            with codecs.open('json/' + name + '.min.json', 'w+', 'utf-8-sig') as file:
                file.write(content)
                print('SUCCESS: File %s.min.%s created!' % (name, 'json'))
        except:
            print('ERROR: Cannot create the output file')
            print(Exception.with_traceback())

Parser(['nvi', 'acf', 'aa', 'apee', 'bbe', 'cornilescu', 'cuv','esperanto','finnish','greek','kjv','ko','ncv','pr','rvr','schlachter','svd','synodal','vietnamese'])