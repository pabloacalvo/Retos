from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, Future
from threading import Thread
from multiprocessing import Process
import time
import os

def fibonnaci(number):
    if number == 1:
        return 0
    if number ==2:
        return 1
    
    return fibonnaci(number-1) + fibonnaci(number-2)

def is_prime(number):
    if number  < 2:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    return number

def show_info(number):
    #print(fibonnaci(number))
    print(is_prime(number))

def validate_future(function):
    def wrapper(future):
        return function(future.result())
    
    return wrapper

@validate_future
def use_prime_number(number):
    print("Vamos a realizar un encrypt con:", number)

# Version usando pools
"""if __name__ == "__main__":
    start = time.time()
    numbers = [700,167449,112889,3842161,4535189]
    tasks = []
    with ProcessPoolExecutor(max_workers=4) as worker:
        for number in numbers:
            worker.submit(show_info,number)
    
    print("Finalizamos el programa: ", time.time()- start)

"""
# Usando pool y futures
if __name__ == "__main__":
    start = time.time()
    cores = os.cpu_count()
    numbers = [2,4,17,20,23,25,31,35,41,42,53,55,59,60,67,69,71,75,83,85,89,90,97,100,101,102,103,105,107,110]
    tasks = []
    # Crear Pool de threads, la cantidad de threads es la cantidad de nucleos
    with ThreadPoolExecutor(max_workers=cores) as worker:
        for number in numbers:
            future = worker.submit(is_prime, number)
            #future.add_done_callback(lambda future: print("El resultado es:", future.result()))
            # Ejemplo si el future devuelve exito, osea es primo, hacemos una tarea
            future.add_done_callback(use_prime_number)

    print("Finalizamos el programa: ", time.time()- start)



# Creando un proceso por cada elemento. Es mas lento
"""if __name__ == "__main__":
    start = time.time()
    numbers = [700,167449,112889,3842161,4535189]
    tasks = []

    for number in numbers:
        process = Process(target=show_info, args=(number,))
        process.start()
        tasks.append(process)

        for task in tasks:
            task.join()
        print("Finalizamos el programa: ", time.time()- start)

"""
# Cantidad de cores
#print(os.cpu_count())
"""
    thread1 = Process(target=is_prime, args=(1_000_000,))
    thread1 = Process(target=is_prime, args=(2,))
    thread2 = Process(target=show_fibonnaci_info, args=(42,))



    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
"""

