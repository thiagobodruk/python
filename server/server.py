import socket,codecs

# Setup
ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
host = ip
port = 3333
conns = 5
# Start Socket Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(conns)

print('Starting Python Server at %s:%i' % (host, port))

# HTML Response
file = open('html/index.html','r')
html = file.read()
html = html.encode('utf-8')

# Listen for Connections
while True:
	conn, addr = s.accept()
	conn.send(html)
	buff = conn.recv(1024)
	
	if len(buff) > 0:
		print(buff.decode('utf-8'))