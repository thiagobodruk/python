import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.6',3333))
text = 'Hello World'
sock.send(text.encode('utf-8'))