import socket
 

s = socket.socket()
s.connect(('192.168.43.53', 9000))
s.send(b'hola desde el cliente')
respuesta=s.recv(1024)
print(respuesta)
s.close()
