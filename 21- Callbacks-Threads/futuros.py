import time
from concurrent.futures import Future, ThreadPoolExecutor
import requests

def hello_world(future):
    print("Hola mundo!!!")
# Estas funciones solo pueden recibir como parametro la intancia de Future
# se pueden utilizar o no sus metodos
def callback(future):
    print("Hola mundo!")

def callback1(future):
    result = future.result()
    print(result)


"""future = Future()
# Funcion que se va ejecutar si el resultado es exitoso, 
# Exitoso = no devuelve errror
future.add_done_callback(hello_world)
future.add_done_callback(callback)
future.add_done_callback(callback1)

time.sleep(3)
# El futuro se va ejecutar si se da un resultado exitoso
future.set_result('Hola pablo')"""




def get_pokemon_name(pokemon_id):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    
    if response.status_code == 200:
        name = response.json().get('forms')[0]['name']
        return name

def validate_future(function):
    def wrapper(future):
        return function(future.result())
    return wrapper

@validate_future
def show_pokemon_name(name):
    print(name)
    
if __name__ == '__main__':
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as worker:
        for n in range(1,101):
            future= worker.submit(get_pokemon_name,n)

            future.add_done_callback(show_pokemon_name)

    
    print("Finalizamos el programa en:", time.time()-start)
