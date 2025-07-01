import time #time.sleep duerme el thread que llama al sleep
from random import randint
import asyncio
import requests


""" 
Corrutinas: funciones que se pueden frenar y reanudar
"""
"""
Una función asíncrona es una función que se define con 
async def y que no se ejecuta inmediatamente cuando se llama, 
sino que devuelve un objeto especial llamado corutina. 
Esta corutina representa una tarea que puede pausarse y reanudarse, 
permitiendo que otras tareas se ejecuten mientras espera. 
"""

# Threads y Asyn -> Concurrencia
                    #-> Async si necesito pausar la ejecucion
# Procesos -> Paralelos

# generadores
def random_numbers_gen(number):
    for _ in range(number):
        print("Antes de pausar")
        yield randint(10,100)
        print("Despues de pausar")

for x in random_numbers_gen(10):
    print(x)


async def funcion_a():
    print("Hola funcion 1")
    await asyncio.sleep(5)
    print("Finalizamos la funcion luego de retomarla")

async def funcion_b():
    print("Hola funcion 2")
    await asyncio.sleep(2)

async def funcion_c():
    print("Hola funcion 3")
    # Esperar 3 segundos
    await asyncio.sleep(5)

# Patron orquestador
async def main():
    task_1 = asyncio.create_task(funcion_a())
    task_2 = asyncio.create_task(funcion_b())
    task_3 = asyncio.create_task(funcion_c())

    # Esperar que se ejecute cada funcion antes de avanzar al print
    # las tres funciones se ejecutan concurrentemente
    #await task_1
    #await task_2
    #await task_3

    await asyncio.gather(
        funcion_a(),
        funcion_b(),
        funcion_c()
    )
    print("Finalizamos el main")

# Las tareas asincronas se ejecutan a la vez
#asyncio.run(main())


def get_pokemon_name(pokemon_id):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    
    if response.status_code == 200:
        name = response.json().get('forms')[0]['name']
        return name
    
async def show_pokemon_info(number):
    name = get_pokemon_name(number)
    print(name)
    
async def main_2():
    tasks = [
        show_pokemon_info(n) for n in range(100)
    ]
    # Espera a la funcion
    await asyncio.gather(*tasks)
    print("Finalizamos")


asyncio.run(main_2())