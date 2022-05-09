import time

def calc_cuadrado(numbers):
    for n in numbers:
        time.sleep(0.2)
        print('cuadrado ' + str(n*n))

def calc_cubo(numbers):
    for n in numbers:
        time.sleep(0.2)
        print('cubo ' + str(n*n*n))


arr=[2,3,8,9]

t = time.time()
calc_cuadrado(arr)
calc_cubo(arr)
print((time.time()-t))
