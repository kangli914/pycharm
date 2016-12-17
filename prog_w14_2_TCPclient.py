# Writing a client program
import socket
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
port = 9999
# connection to hostname on the port.

'''
Note - on client, we don't do socket 'bind' & 'listen'
# bind to the port 
serversocket.bind((host, port)) 

# queue up to 5 requests 
serversocket.listen(5)
'''

s.connect((host, port))
# Receive no more than 1024 bytes
msg = s.recv(1024)
s.close()
print (msg.decode('ascii'))