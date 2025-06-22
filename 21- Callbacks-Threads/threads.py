import time
from time import sleep
from threading import Thread

def function1():
    print("Hola, funcion 1")
    sleep(2)

def function2():
    print("Hola, funcion 2")
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