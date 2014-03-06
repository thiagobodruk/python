#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request

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
		page = urllib.request.urlopen(u)
		html = page.read()
		soup = BeautifulSoup(html)
		for a in soup.find_all('a'):
			try:
				links.append(a['href'])
			except:
				print('ERROR: Cant parse ' + str(a))
		links.sort()
		for l in links:
			print(l + '\n')
			file.write(l + '\n')
	file.close()
options()
crawl()