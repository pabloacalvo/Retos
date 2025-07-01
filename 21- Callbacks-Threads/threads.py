from concurrent.futures import ThreadPoolExecutor
import time
from time import sleep
from threading import Thread

def function1():
    print("Hola, funcion 1")
    sleep(2)

def function2():
    print("Hola, funcion 2")
    sleep(3)

def function3():
    print("Hola, funcion 3")
    sleep(2)

def function4():
    print("Hola, funcion 4")
    sleep(3)
def function5():
    print("Hola, funcion 5")
    sleep(2)

def function6():
    print("Hola, funcion 6")
    sleep(3)

start = time.time()
#function1()
#function2()

# target la funcion que se va ejecutar, name permite asignar nombre al thread
thread1 = Thread(target=function1, name='thread1')
thread2 = Thread(target=function1, name='thread2')

# empezar, va haber 3 el main y estos dos
thread1.start()
thread2.start()


thread1.join() #main thread, espera hasta que el thread1 finalice
thread2.join()


print(time.time() -start)

# Lista de funciones
funtions = [function1,function2,function3,function4,function5,function6]

# Crear Pool de threads
with ThreadPoolExecutor(max_workers=4) as worker:
    for f in funtions:
        worker.submit(f)
    