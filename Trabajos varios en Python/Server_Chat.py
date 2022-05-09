from Tkinter import *
import socket

s = socket.socket()
s.bind(('192.168.43.52',9000))
s.listen(True)
conn, addr = s.accept()
conn.send(b"Conexion iniciada")
resp=conn.recv(1024)
print(resp)

def Enviar():


    msg = campo_de_texto.get()
    conn.send(msg)
    resp2 = conn.recv(1024)
    campo_de_texto2.insert(2, resp2)


while True:


    gui = Tk()
    gui.geometry("500x300+100+100")
    gui.title("Mensaje")
    ################################################
    var1 = StringVar()
    var1.set("Enviar mensaje")
    label1 = Label(gui, textvariable=var1, height=2)
    label1.pack()
    campo_de_texto = Entry(gui)
    campo_de_texto.pack()
    ######################################
    var2 = StringVar()
    var2.set("Mensaje recibido")
    labe22 = Label(gui, textvariable=var1, height=2)
    labe22.pack()
    campo_de_texto2 = Entry(gui)
    campo_de_texto2.pack()
    ######################################
    boton1 = Button(gui, text="Enviar", command=Enviar)
    boton1.pack()
    gui.mainloop()

