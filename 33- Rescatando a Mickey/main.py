"""/*
 * EJERCICIO:
 * ¡Disney ha presentado un montón de novedades en su D23!
 * Pero... ¿Dónde está Mickey?
 * Mickey Mouse ha quedado atrapado en un laberinto mágico
 * creado por Maléfica.
 * Desarrolla un programa para ayudarlo a escapar.
 * Requisitos:
 * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
 * 2. Los valores de las celdas serán:
 *    - ⬜️ Vacío
 *    - ⬛️ Obstáculo
 *    - 🐭 Mickey
 *    - 🚪 Salida
 * Acciones:
 * 1. Crea una matriz que represente el laberinto (no hace falta
 * que se genere de manera automática).
 * 2. Interactúa con el usuario por consola para preguntarle hacia
 * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
 * 3. Muestra la actualización del laberinto tras cada desplazamiento.
 * 4. Valida todos los movimientos, teniendo en cuenta los límites
 * del laberinto y los obtáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.
 */"""


import random

"""_summary_
    random.choice -> Elemento aleatorio de un iterable(lista,tupla,etc)
    random.randint -> Elemento aletorio en un rango de enteros
"""

def created_labyrinth():
    # Crear la matriz de 6x6
    labyrinth = [(['⬜️'] * 6) for _ in range(6)]
    obtacles_position = []
    # Se crean los obstaculos de forma aleatoria
    # PENDIENTE DE REVISION SE ESTA CREANDO OBSTACULOS EN LA MISMA POSICION HACIENDO
    for _ in range(3):
        obstacle = (random.randint(0,5), random.choice([0,5]))
        labyrinth[obstacle[0]][obstacle[1]] = '⬛️'
        obtacles_position.append(obstacle)
    
    # Validacion para Mickey no ocupe el lugar de un obstaculo
    while True:
        mickey_postion = (random.randint(0,5), random.choice([0,5]))
        if mickey_postion not in obtacles_position:
            print(mickey_postion)
            print(obtacles_position)
            break
    
    labyrinth[mickey_postion[0]][mickey_postion[1]] = '🐭'

    
    for row in labyrinth:
        print("".join(map(str,row)))
    return labyrinth


created_labyrinth()
