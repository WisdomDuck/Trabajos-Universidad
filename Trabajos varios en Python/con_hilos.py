import threading
import datetime
import time

def consultar(id_persona):
    time.sleep(2)
    return
def guardar(id_persona, data):
    time.sleep(5)
    return

tiempo_ini = datetime.datetime.now()
h1= threading.Thread(name="hilo_1", target=consultar, args=(1, ))
h2= threading.Thread(name="hilo_2", target=guardar, args=(1, "hola" ))
h1.start()
h2.start()
h1.join()
h2.join()
tiempo_fin = datetime.datetime.now()
print("tiempo:" + str(tiempo_fin.second - tiempo_ini.second))
