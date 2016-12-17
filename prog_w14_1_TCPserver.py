# Writing an Internet server 
import socket 
# create a socket object 

'''
SOCK_STREAM --> for TCP reliable streaming data
SOCK_DGRAM  --> for UDP non-reliabel as data sent by chunk
'''
serversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM) 
# get local machine name 
host = socket.gethostname() 
port = 9999 

'''
'bind': binds socket to address (hostname and port number).
'''
# bind to the port 
serversocket.bind((host, port)) 

# queue up to 5 requests 
serversocket.listen(5)

while True:
	# establish a connection
	'''
	server will need to create another socket than the original socket to send data to client
	
	'clientsocket,addr = serversocket.accept()' this assignment does 2 assignments to variables: 'clientsocket' and 'addr' in one go
	'''
	clientsocket,addr = serversocket.accept()
	print("Got a connection from %s" % str(addr))
	msg='Thank you for connecting'+ "\r\n"
	clientsocket.send(msg.encode('ascii'))
	clientsocket.close()