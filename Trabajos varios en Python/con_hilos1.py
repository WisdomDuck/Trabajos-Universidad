import time
import threading
def calc_square(numbers):
    for n in numbers:
        time.sleep(0.2)
        print('cuadrado ' + str(n*n))
def calc_cube(numbers):
    for n in numbers:
        time.sleep(0.2)
        print('cubo ' + str(n*n*n))

numbers=[2,3,8,9]
t = time.time()
h1 = threading.Thread(target=calc_square, args=(numbers,))
h2 = threading.Thread(target=calc_cube, args=(numbers,))
h1.start()
h2.start()
h1.join()
h2.join()
print(time.time()-t)
