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
function1()
function2()

print(time.time() -start)