#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests, re, urllib

class Crawler:
	
	headers = {'User-Agent' : 'Mozilla/5.0', 'Accept' : '*/*'}
	
	def __init__(self):
		pass
		
	def extra(self, keyword):
		res = []
		url = "http://busca.deliveryextra.com.br/search?w="
		html = self.load(url, keyword)
		# ESTA MERDA NÃO ESTÁ FUNCIONANDO!
		for product in html.findAll('div'):
			print(product.encode('utf-8'))
		return res
	
	def search(self, keyword):
		res = {}
		res['extra'] = self.extra(keyword)
		return res
	
	def load(self, source, keyword=False):
		try:
			url = source + keyword if keyword else source
			html = urllib.request.urlopen(urllib.request.Request(url, None, self.headers)).read()
			soup = BeautifulSoup(html, 'html.parser')
			return soup
		except:
			print('[ERROR] Cannot parse ' + url)