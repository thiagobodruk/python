#!/usr/bin/python

from biblia import Biblia
import json, codecs, sys, getopt, os
import xml.etree.ElementTree as et

class App:
    def __init__(self, argv):
        self.main(argv)

    def main(self, argv):
        help = 'Help:\n\t %s -v <version> -s <start> -e <end> -l <lang>' % __file__
        try:
            opts, args = getopt.getopt(argv, 'v:s:e:l:o:',
                                       ['version=', 'start=', 'end=', 'lang=', 'output=', 'xml', 'sql', 'all', 'cache', 'prefix='])
        except getopt.GetoptError:
            print(help)
            sys.exit(2)
        start, end, lang, json, xml, sql, all, cache, prefix = (0, 66, 'pt', True, False, False, False, False, '')
        for opt, arg in opts:
            if opt in ('-v', '--version'):
                version, output = (arg, arg)
            elif opt in ('-s', '--start'):
                start = arg
            elif opt in ('-e', '--end'):
                end = arg
            elif opt in ('-l', '--lang'):
                lang = arg
            elif opt == '--xml':
                xml, json = (True, False)
            elif opt == '--sql':
                sql, json = (True, False)
            elif opt == '--all':
                all = True
            elif opt == '--cache':
                cache = True
            elif opt == '--prefix':
                prefix = arg + '_'
        try:
            if min == True:
                parse = self.minified(self.cache(version))
            if cache == True:
                parse = self.cache(version)
            else:
                parse = self.parse(version, start, end, lang)
        except:
            print('\n', Exception.with_traceback())
            print(help)
            sys.exit()

        print('\n')
        if xml == True:
            self.save(self.xml(parse), prefix + version, 'xml')
        elif sql == True:
            self.save(self.sql(parse), prefix + version, 'sql')
        elif all == True:
            self.save(self.jsson(parse), prefix + version)
            self.save(self.xml(parse), prefix + version, 'xml')
            self.save(self.sql(parse), prefix + version, 'sql')
        elif json == True:
            self.save(self.json(parse), prefix + version)

    def parse(self, version, start, end, lang):
        b = Biblia()
        biblia = b.buildBible(version, start, end, lang)
        return biblia

    def json(self, content):
        return json.dumps(content, ensure_ascii=False, sort_keys=True)

    def xml(self, content):
        bible = et.Element('bible')
        for book in content:
            b = et.SubElement(bible, 'b', n=book['book'], id=book['abbrev'])
            for chapter in book['chapters']:
                for chap, verses in chapter.items():
                    c = et.SubElement(b, 'c', n=chap)
                    i = 1
                    for i in range(1, len(verses) + 1):
                        v = et.SubElement(c, 'v', n=str(i)).text = verses[str(i)]
                        i += 1
        xml = '<?xml version="1.0" encoding="UTF-8"?>' + et.tostring(bible, encoding='utf-8').decode('utf-8')
        return xml

    def sql(self, content):
        return json.dumps(content, ensure_ascii=False, sort_keys=True)

    def save(self, content, name, extension='json'):
        try:
            with codecs.open(extension + '/' + name + '.' + extension, 'w+', 'utf-8-sig') as file:
                file.write(content)
                print('SUCCESS: File %s.%s created!' % (name, extension))
        except:
            print('ERROR: Cannot create the output file')

    def cache(self, version):
        try:
            data = codecs.open('json/' + version + '.json', 'r', 'utf-8-sig').read()
            return json.loads(data)
        except:
            sys.exit('ERROR: Cannot load cache from %s.json' % version)

if __name__ == "__main__":
    App(sys.argv[1:])