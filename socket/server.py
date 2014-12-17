import socket

ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
port = 3333

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, port))
sock.listen(5)
print('Starting server at %s:%s...\n' % (ip, port))

while True:
	conn, addr = sock.accept()
	buff = conn.recv(1024)
	if len(buff) > 0:
		print(buff.decode('utf-8'))