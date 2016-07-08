#!/usr/bin/python

import urllib.request, re, sys
from urllib.parse import quote

class Biblia:
    chars = r"([^<>]+)"
    books = [{"abbrev-pt": "gn", "abbrev-en": "gn", "chapters": 50, "pt": "Gênesis", "en": "Genesis"},
             {"abbrev-pt": "ex", "abbrev-en": "ex", "chapters": 40, "pt": "Êxodo", "en": "Exodus"},
             {"abbrev-pt": "lv", "abbrev-en": "lv", "chapters": 27, "pt": "Levítico", "en": "Leviticus"},
             {"abbrev-pt": "nm", "abbrev-en": "nm", "chapters": 36, "pt": "Números", "en": "Numbers"},
             {"abbrev-pt": "dt", "abbrev-en": "dt", "chapters": 34, "pt": "Deuteronômio", "en": "Deuteronomy"},
             {"abbrev-pt": "js", "abbrev-en": "js", "chapters": 24, "pt": "Josué", "en": "Joshua"},
             {"abbrev-pt": "jz", "abbrev-en": "jud", "chapters": 21, "pt": "Juízes", "en": "Judges"},
             {"abbrev-pt": "rt", "abbrev-en": "rt", "chapters": 4, "pt": "Rute", "en": "Ruth"},
             {"abbrev-pt": "1sm", "abbrev-en": "1sm", "chapters": 31, "pt": "1 Samuel", "en": "1 Samuel"},
             {"abbrev-pt": "2sm", "abbrev-en": "2sm", "chapters": 24, "pt": "2 Samuel", "en": "2 Samuel"},
             {"abbrev-pt": "1rs", "abbrev-en": "1kgs", "chapters": 22, "pt": "1 Reis", "en": "1 Kings"},
             {"abbrev-pt": "2rs", "abbrev-en": "2kgs", "chapters": 25, "pt": "2 Reis", "en": "2 Kings"},
             {"abbrev-pt": "1cr", "abbrev-en": "1ch", "chapters": 29, "pt": "1 Crônicas", "en": "1 Chronicles"},
             {"abbrev-pt": "2cr", "abbrev-en": "2ch", "chapters": 36, "pt": "2 Crônicas", "en": "2 Chronicles"},
             {"abbrev-pt": "ed", "abbrev-en": "ezr", "chapters": 10, "pt": "Esdras", "en": "Ezra"},
             {"abbrev-pt": "ne", "abbrev-en": "ne", "chapters": 13, "pt": "Neemias", "en": "Nehemiah"},
             {"abbrev-pt": "et", "abbrev-en": "et", "chapters": 10, "pt": "Ester", "en": "Esther"},
             {"abbrev-pt": "jó", "abbrev-en": "job", "chapters": 42, "pt": "Jó", "en": "Job"},
             {"abbrev-pt": "sl", "abbrev-en": "ps", "chapters": 150, "pt": "Salmos", "en": "Psalms"},
             {"abbrev-pt": "pv", "abbrev-en": "prv", "chapters": 31, "pt": "Provérbios", "en": "Proverbs"},
             {"abbrev-pt": "ec", "abbrev-en": "ec", "chapters": 12, "pt": "Eclesiastes", "en": "Ecclesiastes"},
             {"abbrev-pt": "ct", "abbrev-en": "so", "chapters": 8, "pt": "Cânticos", "en": "Song of Solomon"},
             {"abbrev-pt": "is", "abbrev-en": "is", "chapters": 66, "pt": "Isaías", "en": "Isaiah"},
             {"abbrev-pt": "jr", "abbrev-en": "jr", "chapters": 52, "pt": "Jeremias", "en": "Jeremiah"},
             {"abbrev-pt": "lm", "abbrev-en": "lm", "chapters": 5, "pt": "Lamentações de Jeremias",
              "en": "Lamentations"},
             {"abbrev-pt": "ez", "abbrev-en": "ez", "chapters": 48, "pt": "Ezequiel", "en": "Ezekiel"},
             {"abbrev-pt": "dn", "abbrev-en": "dn", "chapters": 12, "pt": "Daniel", "en": "Daniel"},
             {"abbrev-pt": "os", "abbrev-en": "ho", "chapters": 14, "pt": "Oséias", "en": "Hosea"},
             {"abbrev-pt": "jl", "abbrev-en": "jl", "chapters": 3, "pt": "Joel", "en": "Joel"},
             {"abbrev-pt": "am", "abbrev-en": "am", "chapters": 9, "pt": "Amós", "en": "Amos"},
             {"abbrev-pt": "ob", "abbrev-en": "ob", "chapters": 1, "pt": "Obadias", "en": "Obadiah"},
             {"abbrev-pt": "jn", "abbrev-en": "jn", "chapters": 4, "pt": "Jonas", "en": "Jonah"},
             {"abbrev-pt": "mq", "abbrev-en": "mi", "chapters": 7, "pt": "Miquéias", "en": "Micah"},
             {"abbrev-pt": "na", "abbrev-en": "na", "chapters": 3, "pt": "Naum", "en": "Nahum"},
             {"abbrev-pt": "hc", "abbrev-en": "hk", "chapters": 3, "pt": "Habacuque", "en": "Habakkuk"},
             {"abbrev-pt": "sf", "abbrev-en": "zp", "chapters": 3, "pt": "Sofonias", "en": "Zephaniah"},
             {"abbrev-pt": "ag", "abbrev-en": "hg", "chapters": 2, "pt": "Ageu", "en": "Haggai"},
             {"abbrev-pt": "zc", "abbrev-en": "zc", "chapters": 14, "pt": "Zacarias", "en": "Zechariah"},
             {"abbrev-pt": "ml", "abbrev-en": "ml", "chapters": 4, "pt": "Malaquias", "en": "Malachi"},
             {"abbrev-pt": "mt", "abbrev-en": "mt", "chapters": 28, "pt": "Mateus", "en": "Matthew"},
             {"abbrev-pt": "mc", "abbrev-en": "mk", "chapters": 16, "pt": "Marcos", "en": "Mark"},
             {"abbrev-pt": "lc", "abbrev-en": "lk", "chapters": 24, "pt": "Lucas", "en": "Luke"},
             {"abbrev-pt": "jo", "abbrev-en": "jo", "chapters": 21, "pt": "João", "en": "John"},
             {"abbrev-pt": "atos", "abbrev-en": "act", "chapters": 28, "pt": "Atos", "en": "Acts"},
             {"abbrev-pt": "rm", "abbrev-en": "rm", "chapters": 16, "pt": "Romanos", "en": "Romans"},
             {"abbrev-pt": "1co", "abbrev-en": "1co", "chapters": 16, "pt": "1 Coríntios", "en": "1 Corinthians"},
             {"abbrev-pt": "2co", "abbrev-en": "2co", "chapters": 13, "pt": "2 Coríntios", "en": "2 Corinthians"},
             {"abbrev-pt": "gl", "abbrev-en": "gl", "chapters": 6, "pt": "Gálatas", "en": "Galatians"},
             {"abbrev-pt": "ef", "abbrev-en": "eph", "chapters": 6, "pt": "Efésios", "en": "Ephesians"},
             {"abbrev-pt": "fp", "abbrev-en": "ph", "chapters": 4, "pt": "Filipenses", "en": "Philippians"},
             {"abbrev-pt": "cl", "abbrev-en": "cl", "chapters": 4, "pt": "Colossenses", "en": "Colossians"},
             {"abbrev-pt": "1ts", "abbrev-en": "1ts", "chapters": 5, "pt": "1 Tessalonicenses",
              "en": "1 Thessalonians"},
             {"abbrev-pt": "2ts", "abbrev-en": "2ts", "chapters": 3, "pt": "2 Tessalonicenses",
              "en": "2 Thessalonians"},
             {"abbrev-pt": "1tm", "abbrev-en": "1tm", "chapters": 6, "pt": "1 Timóteo", "en": "1 Timothy"},
             {"abbrev-pt": "2tm", "abbrev-en": "2tm", "chapters": 4, "pt": "2 Timóteo", "en": "2 Timothy"},
             {"abbrev-pt": "tt", "abbrev-en": "tt", "chapters": 3, "pt": "Tito", "en": "Titus"},
             {"abbrev-pt": "fm", "abbrev-en": "phm", "chapters": 1, "pt": "Filemom", "en": "Philemon"},
             {"abbrev-pt": "hb", "abbrev-en": "hb", "chapters": 13, "pt": "Hebreus", "en": "Hebrews"},
             {"abbrev-pt": "tg", "abbrev-en": "jm", "chapters": 5, "pt": "Tiago", "en": "James"},
             {"abbrev-pt": "1pe", "abbrev-en": "1pe", "chapters": 5, "pt": "1 Pedro", "en": "1 Peter"},
             {"abbrev-pt": "2pe", "abbrev-en": "2pe", "chapters": 3, "pt": "2 Pedro", "en": "2 Peter"},
             {"abbrev-pt": "1jo", "abbrev-en": "1jo", "chapters": 3, "pt": "1 João", "en": "1 John"},
             {"abbrev-pt": "2jo", "abbrev-en": "2jo", "chapters": 1, "pt": "2 João", "en": "2 John"},
             {"abbrev-pt": "3jo", "abbrev-en": "3jo", "chapters": 1, "pt": "3 João", "en": "3 John"},
             {"abbrev-pt": "jd", "abbrev-en": "jd", "chapters": 1, "pt": "Judas", "en": "Jude"},
             {"abbrev-pt": "ap", "abbrev-en": "re", "chapters": 22, "pt": "Apocalipse", "en": "Revelation"}]

    def __init__(self):
        pass

    def buildBible(self, version, start=0, end=66, lang='pt'):
        b = []
        for book in range(int(start), int(end)):
            res = self.buildBook(version, book, lang)
            b.append(res)
        return b

    def buildBook(self, version, book, lang='pt'):
        b = []
        i = 1;
        print('Parsing %s...' % self.books[book][lang])
        sys.stdout.flush()
        for chapter in range(1, self.books[book]['chapters'] + 1):
            c = self.buildChapter(version, self.books[book]['abbrev-pt'], chapter)
            #b.append({i: c})
            b.append(c)
            i += 1
        res = {'abbrev': self.books[book]['abbrev-' + lang], 'name': self.books[book][lang], 'chapters': b}
        return res

    def buildChapter(self, version, book, chapter):
        #res = {}
        res = []
        verses = self.parseHTML(version, book, chapter)
        i = 1;
        for verse in verses:
            verse = verse.replace('&quot;', '"')
            #res[i] = verse
            res.append(verse)
            try:
                print('[%s %s:%s] %s' % (book.title(), chapter, i, verse))
            except:
                print('[%s %s:%s] ERROR: Encoding issue' % (book, chapter, i))
            sys.stdout.flush()
            i += 1
        return res

    def parseHTML(self, version, book, chapter):
        regex = "<span class=\"text\">%s<\/span>" % self.chars
        url = 'http://ie8.bibliaonline.com.br/%s/%s/%s' % (version, quote(book), chapter)
        try:
            page = urllib.request.urlopen(url)
        except:
            print('ERROR: Cannot open %s' % url)
            sys.exit()
        html = page.read().decode('utf-8')
        verses = re.findall(regex, html)
        return verses