#! /bin/python3

import traceback
import urllib.request
import urllib.parse
import hashlib
import json
from pprint import pprint

tk = None
js = None
url = 'https://plugapps.net/whatsee/api/'

def login():
	print('[Login] Starting...')
	#user = input('user: ')
	#password = input('pass: ')
	user = 'mr.bean@gmail.com'
	pw = '123456'
	pw = hashlib.sha1(pw.encode('utf-8'))	
	pr = urllib.parse.urlencode({'user' : user, 'pass' : pw.hexdigest()}).encode('utf-8')	
	r = urlPOST(url + 'user/login', pr)
	js = parseJson(r)
	global tk 
	tk = js.get('response').get('token')
	print('[Login] Token: %s' % (tk))

def feed():
	print('[Feed] Starting...')
	n = True
	i = 1
	feed = []
	while n:
		r = urlGET(url + 'feed/timeline/%i/%s' % (i, tk))
		if r:
			js = parseJson(r)
			rs = js.get('response')
			for p in rs:
				feed.append(p)
			i = i + 1
		else:
			n = False
	print('[Feed] %i objects found...' % (len(feed)))
	for p in feed:
		print('\n')
		print('Text: %s' % (p.get('text')))
		print('Image: %s/%s' % (url, p.get('image')))
		print('Date: %s' % (p.get('date')))
		print('Status: %s' % (p.get('status')))
	
def urlPOST(u, p):
	try:
		f = urllib.request.urlopen(u, p)
		c = f.read()
		f.close()
		return c.decode('utf-8')
	except Exception as e:
		print('[POST] Error: %s' % (u))
		return False
		
def urlGET(u):
	try:
		f = urllib.request.urlopen(u)
		c = f.read()
		f.close()
		return c.decode('utf-8')
	except Exception as e:
		print('[GET] Error: %s' % (u))
		return False

def parseJson(j):
	try:
		data = json.loads(j)
		return data
	except:
		print('[JSON] Error: %s' % (j))
login()
feed()