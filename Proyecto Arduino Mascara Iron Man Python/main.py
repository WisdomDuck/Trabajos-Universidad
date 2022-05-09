
from tkinter import *
import serial
import time

def encender():
 arduino = serial.Serial("COM3", 9600)
 time.sleep(2)
 arduino.write(b'1')
 arduino.close()

def apagar():
 arduino = serial.Serial("COM3", 9600)
 time.sleep(2)
 arduino.write(b'0')
 arduino.close()

gui = Tk()
gui.title("control led")
gui.geometry("400x250")

boton1 = Button(gui, text = "ENCENDER", command = encender,width=15)
boton1.pack()

boton2 = Button(gui, text = "APAGAR", command = apagar,width=15)
boton2.pack()

gui.mainloop()
