import socket

s = socket.socket()
s.bind(('192.168.43.52',5007))
s.listen(True)


print("PROGRAMA")
a = input("ingresar primer numero:")
b = input("ingresar segundo numero:")
suma= str(a + b)

while True:
    conn, addr = s.accept()
    print ('Conexion con direccion:', addr)
    conn.send(suma) 
conn.close()
