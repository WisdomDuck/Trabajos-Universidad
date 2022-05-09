from Tkinter import *
#import serial
import time
import socket

s = socket.socket()
s.bind(('192.168.43.52',9000))
s.listen(True)
conn, addr = s.accept()
resp=conn.recv(1024)
print(resp)

def sec():

    conn.send(b'Hola soy el servidor')

    conn.send(b'1')

    numero1=conn.recv(1024)

    #abel(gui, text = numero1 ).pack()

    tkinter.message.showinfo("numero",numero1 )
    #ent= Entry(gui, text=numero1)

    conn.close()

def hil():
    conn.send(b'Hola soy el servidor')

    conn.send(b'2')

    numero1 = conn.recv(1024)

    Label(gui, text = numero1).pack()

    conn.close()


gui = Tk()
gui.title("FUNCIONES SECUENCIALES E HILOS")
gui.geometry("400x250")


boton1 = Button(gui, text = "SECUENCIAL", command = sec,width=15)
boton1.pack()

boton2 = Button(gui, text = "HILOS", command = hil,width=15)
boton2.pack()

gui.mainloop()
