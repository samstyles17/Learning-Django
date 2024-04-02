import socket

# socket.socket basically means create a  phone
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server at specific port number
mysock.connect(('data.pr4e.org',80))
# follows the telnet pattern of fetching the page
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while(True):
	data = mysock.recv(512)
	if len(data) < 1:
		break
	print(data.decode(), end='')
#close the  socket connection
mysock.close()
