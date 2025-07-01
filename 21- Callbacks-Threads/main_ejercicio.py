"""
/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
 */"""

import random
import time
import threading

def create_order(dish_name:str,simulate_sleep,dish_confirm,order_ready,delivered_order):
    def process():
        waiting_time = 0
        print(f"Comenzando el pedido, plato seleccionado: {dish_name}")
        
        waiting_time += simulate_sleep()
        print(f'Pedido {dish_name} procesado en: {waiting_time} segundos')
        dish_confirm(dish_name)
        
        waiting_time += simulate_sleep()
        print(f'Pedido {dish_name} procesado en: {waiting_time} segundos')
        order_ready(dish_name)

        waiting_time += simulate_sleep()
        delivered_order(dish_name)
        print(f'Pedido {dish_name} terminado en: {waiting_time} segundos')
    
    threading.Thread(target=process).start()
    


def dish_confirm(dish_name):
    print(f"Plato {dish_name} confirmado")

def order_ready(dish_name):
    print(f"Orden: {dish_name}. Lista")

def delivered_order(dish_name):
    print(f"Orden: {dish_name}. ENTREGADA")

def simulate_sleep():
    sleep = random.randint(1,10)
    time.sleep(sleep)
    return sleep


create_order('Fideos con salsa bolognesa', simulate_sleep,dish_confirm,order_ready,delivered_order)
create_order('Milanesas con pure', simulate_sleep,dish_confirm,order_ready,delivered_order)
create_order('Pizza cuatro quesos', simulate_sleep,dish_confirm,order_ready,delivered_order)
create_order('Hamburguesa Del Toro', simulate_sleep,dish_confirm,order_ready,delivered_order)