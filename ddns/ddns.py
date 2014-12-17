import socket, urllib.request

# Config
host = 'mydomain.ddns.net'
user = 'user'
pasw = 'pass'
ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
url = 'http://'+user+':'+pasw+'@dynupdate.no-ip.com/nic/update?hostname=' + host + '&myip=' + ip

print('Starting DDNS %s @ %s...\n' % (host, ip))

# Process
request = urllib.request.urlopen(url).read()
response = str(request.decode('utf-8'))
print('Status: ' + response)

# Exception
print('Status: Error!')