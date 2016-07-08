#!/usr/bin/python
import socket
import urllib.request
import requests
from datetime import datetime

target = 'http://192.168.1.5:8080/api/downloads'
ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
host, port, conns, s = [ip, 80, 5, socket.socket(socket.AF_INET, socket.SOCK_STREAM)]
s.bind((host, port))
s.listen(conns)
print('Python Server at %s:%i' % (host, port))

json = urllib.request.urlopen(target).read().decode('utf-8')
response = ['HTTP/1.1 200 OK\nContent-Type: text/json\n\n', json]
response = ''.join(response)

while True:
    conn, addr = s.accept()
    conn.send(response.encode('utf-8'))
    buff = conn.recv(1024)
    if len(buff) > 0:
        print(buff.decode('utf-8'))
    conn.close()
