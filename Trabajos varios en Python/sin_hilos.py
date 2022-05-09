import time
import datetime

def consultar(id_persona):
    time.sleep(2)
    return
def guardar(id_persona, data):
    time.sleep(5)
    return

tiempo_ini = datetime.datetime.now()

consultar(1)
guardar(1,"hola")
tiempo_fin = datetime.datetime.now()
print("tiempo:" + str(tiempo_fin.second - tiempo_ini.second))
