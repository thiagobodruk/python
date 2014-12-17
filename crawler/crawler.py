#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import re

url = []
 
def readList():
	try:
		list = open('list.txt', 'r')
		for line in list:
			url.append(line)
	except:
		print('Cannot open the file list.txt!')

def readUrl():
	u = input('URL: ')
	if not(re.search('http',u)):
		u = 'http://' + u
	url.append(u)

def readPage():
	html = page.read()
	page.close()
	soup = BeautifulSoup(html)

def options():
	print('Web Crawler v1.0\n')
	o = int(input('[1] Crawl from List \n[2] Crawl from URL\n\nOption:'))
	if(o == 1):
		readList()
	if(o == 2):
		readUrl()

def crawl():
	file = open('links.txt', 'w+')
	for u in url:
		links = []
		final = []
		u = re.sub('\n$', '', u)
		page = urllib.request.urlopen(u)
		html = page.read()
		soup = BeautifulSoup(html)
		for a in soup.find_all('a'):
			try:
				if(re.search('http', a['href'])):
					links.append(a['href'])
				else:
					href = u + a['href']
					links.append(href)				
			except:
				print('ERROR: Cant parse ' + str(a))
		final = sorted(set(links))
		for l in final:
			if(l != '#' and l != '/'):
				print(l + '\n')
				file.write(l + '\n')
	file.close()
options()
crawl()