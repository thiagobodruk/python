import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 3333))
sock.listen(5) # become a server socket, max 5 conns
print('Starting server...\n')

while True:
	conn, addr = sock.accept()
	buff = conn.recv(1024)
	if len(buff) > 0:
		print(buff.decode('utf-8'))