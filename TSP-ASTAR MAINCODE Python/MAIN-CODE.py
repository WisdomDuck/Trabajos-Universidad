import time
import csv
import os
# funcion para saber si quedan ciudades por visitar
def revision(lista_city, cit):
    for m in range(int(cit)):
        if lista_city[m][0] != 0:
            return 1
    return 0
# funcion para determinar el segundo camino mas corto de la primera ciudad
# solo sirve para la heuristica y la determinacion de el F mas pequeño
def segundo_mas_corto( cant_c ):
    aux_sum1 = 1000000
    coor = 0
    for i in range(cant_c):
        if matriz[0][i] != 0 and matriz[0][i] < aux_sum1:  # cambiar a -1 el punto de iniciacion
            aux_sum1 = matriz[0][i]
            coor = i
    aux_sum2 = 1000000
    # segundo camino de menor costo
    for j in range(cant_c):
        if matriz[0][j] != 0 and matriz[0][j] < aux_sum2 and coor != j:
            aux_sum2 = matriz[0][j]
    return aux_sum2/2
# revisaremos el camino ma corto del nodo en revision (que es un extremo)
# revisaremos 2 costes menores de los nodos faltantes a revisar sumandolos y dividiendolos
# Heuristica In-Out
def heu(punto_ini, lista_ciu, cantidad_c):

    # primero tomaremos los menores valores de los puntos iniciales
    aux_sum1 = 1000000
    # guardaremos en una variale el nodo de menor coste para que en la segunda iteracion (que es la que necesitamos)
    # no se repita
    coor = 0
    # primer camino de manor costo
    for i in range(cantidad_c):
        if matriz[punto_ini][i] != 0 and matriz[punto_ini][i] < aux_sum1:  # cambiar a -1 el punto de iniciacion
            aux_sum1 = matriz[punto_ini][i]
            coor = i
    aux_sum2 = 1000000
    # segundo camino de menor costo
    for j in range(cantidad_c):
        if matriz[punto_ini][j] != 0 and matriz[punto_ini][j] < aux_sum2 and coor != j:
            aux_sum2 = matriz[punto_ini][j]

    # recorro todas las demas ciudades
    for r in range(cantidad_c):

        aux_sum3 = 1000000
        aux_sum4 = 1000000
        coor = 0
        # si no estan en la lista abierta no las voy a recorrer
        if lista_ciu[r][0] != 0:
            for i in range(cantidad_c):  # tomamos los 2 caminos posibles de menor costo
                # si la ciudad no se esta revisanco consigo misma y el camino es a revisar es menor que la variable
                if matriz[lista_ciu[r][0]-1][i] != 0 and matriz[lista_ciu[r][0]-1][i] < aux_sum3:
                    aux_sum3 = matriz[lista_ciu[r][0]-1][i]
                    coor = i
            for j in range(cantidad_c):
                # si la ciudad no se esta revisanco consigo misma y el camino es a revisar es menor que la variable
                # y no es el mismo camino revisado ya con anterioridad
                if matriz[lista_ciu[r][0]-1][j] != 0 and matriz[lista_ciu[r][0]-1][j] < aux_sum4 and coor != j:
                    aux_sum4 = matriz[lista_ciu[r][0]-1][j]
            aux_in_out = aux_sum2 + aux_sum3 + aux_sum4

    return aux_in_out/2

# abrimos el archivo
print("Ingrese el nombre del archivo:")
nombre = input()
arch = open(nombre, 'r')
# guardamos la cantidad de ciudades existentes
res = arch.readline()
# creamos una matriz de distancia para cada ciudad
# creamos 2 listas una en donde estaran las ciudades a revisas (abierto) y la otra el camino ya recorrido (cerrado)

matriz = []
abierto = []
cerrado = []
res = int(res)
# en esta variable contaremos la cantidad de nods expandidos
expandidos = 0
# creamos y agregamos valores en las listas y matrices
for i in range(res):
    matriz.append([0]*res)

for i in range(res):
    abierto.append([0]*3)

for i in range(res):
    L = arch.readline()
    city, x, y = L.split(" ")
    abierto[i][0] = int(city)
    abierto[i][1] = int(x)
    abierto[i][2] = int(y)

for i in range(res):
    x = abierto[i][1]
    y = abierto[i][2]
    for j in range(res):
        z = abierto[j][1]
        w = abierto[j][2]
        matriz[i][j] = abs(int(x)-int(z))+abs(int(y)-int(w))

# cerramos el archivo ya que no lo vamos a utilizar mas
arch.close()

f = 0
# este auxiliar nos ayudara  aposicionarnos en el nodo que revisaremos sin la necesidad de entrar en la lista
aux_a = abierto[0][0]-1
# agregamos la primera ciudad a la lista la cual comenzaremos a recorrer
cerrado.append(abierto[0][0])
# tomaremos el segundo camino más corto del primer nodo para el modelamiento de la heuristica
heu_ini = segundo_mas_corto(res)
# quitamos el nodo inicial de la lista para que no se repita
abierto[0][0] = 0
# iniciamos una variable para terminar la busqueda
No_more = 1
# inicializamos una variable que contrndra la proxima ciudad con el menor F
hold_nodo = 0
# iniciamos una variable que tendra nuestro coste totad de camino
coste_total = 0
# con estas variables veremos el inicio del tiempo de ejecucion de mi codigo
start_time = time.time()
while No_more != 0:
    # variable de coste la cuals nos sera util para guardar los costes de f de las ciudades y decidir el menos costoso
    coste_m = 1000000
    # ciclo para revisar cada ciudad de la lista
    for i in range(int(res)):
        # si la ciudad no se ha visitado y no se compara con si misma y es menor al coste guardado en la variable
        if abierto[i][0] != 0 and matriz[aux_a][i] != 0 and matriz[aux_a][i]+heu(aux_a, abierto, res)+heu_ini < coste_m:
            # guardamos el coste minimo
            coste_m = matriz[aux_a][i]+heu(aux_a, abierto, res) + heu_ini
            # guardamos el nodo de menor F en la variable
            hold_nodo = i
        # solo si el nodo está en la lista de abierto será capaz de aumentar la variable
        if abierto[i][0] != 0:
            expandidos = expandidos + 1
    # agregamos el nodo a la lista de los establecidos
    cerrado.append(hold_nodo+1)
    # quitamos de la list al nodo por recorrer
    abierto[hold_nodo][0] = 0
    # guardamos el nodo en un auxiliar para que este mismo sea el siguiente a comparar
    aux_a = hold_nodo
    # guardamos en una variable el total de F
    coste_total = coste_m + coste_total
    # revisamos si es que quedan nodos a comparar
    No_more = revision(abierto, res)
# con esta variable veremos el tiempo final de la busqueda del codigo
end_time = time.time() - start_time
print("Solucion de el archivo: ", cerrado)
print("Coste total del recorrido: ", coste_total)
print("Nodos expandidos: ", expandidos)
print("Tiempo de ejecucion: ", end_time)


with open('DamaryLobos_GabrielGonzalez_resultados.csv', 'w') as file:
    csv_writer = csv.writer(file, delimiter='-')
    csv_writer.writerow([' Ciudades: ' + str(res), ' Solucion: ' + str(cerrado), ' Nodos expandidos: ' + str(expandidos), ' Tiempo de ejecución: ' + str(end_time)])