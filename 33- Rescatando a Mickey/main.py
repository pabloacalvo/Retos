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
def juego_version1():
    laberinto = [
                ['🐭','⬛️','⬛️','⬛️','⬛️','🚪'],
                ['⬜️','⬜️','⬜️','⬛️','⬜️','⬜️'],
                ['⬛️','⬛️','⬜️','⬛️','⬜️','⬛️'],
                ['⬜️','⬜️','⬜️','⬛️','⬜️','⬛️'],
                ['⬛️','⬜️','⬛️','⬛️','⬜️','⬛️'],
                ['⬛️','⬜️','⬜️','⬜️','⬜️','⬛️']
                ]
    def print_labyrinth():
        for row in laberinto:
            print("".join(map(str,row)))

    mickey = [0,0]



    print(f'Bienvenido al Laberinto de Mikey\n')
    while True:
        current_row, current_column = mickey
        new_row, new_column = current_row, current_column
        print_labyrinth()
        print(f'Selecciona una direccion donde deseas moverte:\n\t[A]Izquierda [D]Derecha [W]Arriba [S]Abajo')
        movement = input()
        match movement:
            case 'a':
                new_column -= 1
            case 'd':
                new_column += 1
            case 'w':
                new_row -= 1
            case 's':
                new_row += 1
            case _:
                print("Opcion incorrecta")
                continue
        
        if new_row  > 5 or new_column > 5 or new_row < 0 or new_column < 0:
            print("No te podes mover en esta direccion")
            continue
        else:
            if '⬛️' in laberinto[new_row][new_column]:
                print("Hay un obstaculo en esta direccion.")
                continue
            elif '🚪' in laberinto[new_row][new_column]:
                print("Ganaste!!!. Salvaste a Mickey")
                break
            else:
                laberinto[current_row][current_column] = '⬜️'
                laberinto[new_row][new_column] = '🐭'
                mickey = new_row, new_column
                continue


def created_labyrinth():
    # Crear la matriz de 6x6
    labyrinth = [(['⬛️'] * 6) for _ in range(6)]
    labyrinth[0][0] = '🐭'
    road = []
    # Se crean los obstaculos de forma aleatoria
    # PENDIENTE DE REVISION SE ESTA CREANDO OBSTACULOS EN LA MISMA POSICION HACIENDO
    for _ in range(8):
        new_road_row, new_road_column = random.randint(0,5), random.choice([0,5])
        old_road_row, old_road_column = new_road_row,new_road_column
        if [new_road_row, new_road_column] in road:
            labyrinth[new_road_row][new_road_column]
            continue
        if labyrinth[new_road_row][new_road_column] == '🚪':
            continue
        elif labyrinth[new_road_row][new_road_column] == '⬛️':
            labyrinth[new_road_row][new_road_column] = '⬜️'
            road.append([old_road_row,old_road_column])
            #print(road)

    
    for row in labyrinth:
        print("".join(map(str,row)))
    return labyrinth


created_labyrinth()
