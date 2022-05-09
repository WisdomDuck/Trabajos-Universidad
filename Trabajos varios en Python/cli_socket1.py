import socket
  
s = socket.socket()
s.connect(('192.168.43.53', 5007))
data = (s.recv(1024))
print ('dato recibido:   ' + str(data))
s.close()
