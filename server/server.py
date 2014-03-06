import socket,codecs

host = 'localhost'
port = 80
conns = 5

# Start Socket Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(conns)

print('Starting Python Server...\n')

# HTML Response
file = open('html/index.html','r')
html = file.read()
html = html.encode('utf-8')

# Listen for Connections
while True:
	conn, addr = s.accept()
	buff = conn.recv(1024)
	conn.send(html)
	
	if len(buff) > 0:
		print(buff.decode('utf-8'))