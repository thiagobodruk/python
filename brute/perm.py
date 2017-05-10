#!/usr/bin/python
import itertools, hashlib, math

class Words:

    def __init__(self, size, chars = None):
        if chars == None:
            self.chars = '01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ'
        else:
            self.chars = chars
        print('%d combinations' % self.getLength(size))
        #self.make(size, chars)

    def getLength(self, size):
        res = []
        for i in range(1, size+1):
            res.append(math.pow(len(self.chars), i))
        return sum(res)

    def getMD5(self, text):
        m = hashlib.md5()
        m.update(text.encode('utf-8'))
        return m.hexdigest()

    def make(self, size):
        with open('res.txt', 'w+') as file:
            for i in range(1, size+1):
                prod = itertools.product(self.chars, repeat=i)

                for j, r in enumerate(prod):
                    text = ''.join(r)
                    md5 = self.getMD5(text)
                    res = text+'\t'+md5
                    print(res + ' %.3f%%' % ((j+1)/float(self.getLength(size))*100))

Words(6)
