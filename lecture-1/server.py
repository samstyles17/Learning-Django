from socket import *

def createServer():
	#Creating the phone 
	serversocket = socket(AF_INET, SOCK_STREAM)
	try:
		# I am willing  to receive phone call o port 9000
		serversocket.bind(('localhost',9000))
		#if the server is busy handling 1 phone call, 4 more calls to the server can be queued
		serversocket.listen(5)
		while(1):
			#This line only runs when the phone call is received
			(clientsocket, address) = serversocket.accept()
			# 5000 characters, decode utf-8 for unicode
			rd = clientsocket.recv(5000).decode()
			pieces = rd.split("\n")
			if len(pieces) > 0:
				print(pieces[0])
			data = "HTTP/1.1 200 OK\r\n"
			data += "Content-Type: text/html; charset=utf-8\r\n"
			data += "\r\n"
			data += "<html><body>Hello World</body></html>\r\n\r\n"
			clientsocket.sendall(data.encode())
			#After the data send ,  client calls shuts down
			clientsocket.shutdown(SHUT_WR)
	except KeyboardInterrupt:
		print("\nShutting Down ... \n")
	except Exception as exc:
		print("\nError:...\n")
		print(exc)
	serversocket.close()

print('Access http://localhost:9000')
createServer()
