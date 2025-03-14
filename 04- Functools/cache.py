from functools import cache
import time
"""
Sirve para guardar resultados en cache y al tener valores previamente procesados la ejecucion
es en menor tiempo.
En este ejemplo primero de procesan del 1 al 20 y luego al procesar el 21 no es necesario repetir los anteriores, solamente 
procesa con el 21 
"""

@cache
def factorial(n):
    print(f"Llamado de la funcion con el valor {n}")
    if n == 1:
        print(f"El resultado de la funcion con valor {n} = {1}")
        return 1
    
    x = n * factorial(n-1)
    print(f"El resultado de la funcion con valor {n} = {x}")
    return x

tic = time.time()
print(f"Resultado: {factorial(20)}")
print(factorial.cache_info())
print((time.time() - tic) * 60)
print("------------------")

tic = time.time()
print(f"Resultado: {factorial(21)}")
print(factorial.cache_info())
print((time.time() - tic) * 60)
print("------------------")