"""*
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
 */
"""

import random
import time
deadpool_health = int(input("Ingresa la vida de Deadpool: "))
wolverine_health = int(input("Ingresa la vida de Wolverine: "))

turn = 0
regenerate = False

while deadpool_health > 0 < wolverine_health:
    turn += 1
    print(f'\nTurno {turn}')

    # Deadpool ataca a Wolweine
    if regenerate:
        print("Deadpool se esta regenerando depues de recibir un golpe critico")
        regenerate = False
    # Genera un numero aliatorio del 1 al 0
    elif random.random() > 0.2:

        deadpool_damage = random.randint(10,100)
        print(f'Deadpool ataca y causa {deadpool_damage} de daño.')
        if deadpool_damage > 80:
            print(f"Golpe critico!!! Deadpool ataca con su daño maximo: {deadpool_damage} Wolverine no podra atacar, se tiene que regenerar.")
            regenerate = True
        
        wolverine_health -= deadpool_damage
        

        if wolverine_health <= 0:
            print("Vida de Wolverine llego a 0")
            break
        else:
            print(f"Vida restante de Wolwerine: {wolverine_health}")
    
    else:
        print("Wolverine esquiva el ataque de Deadpool!!!!")


    # Wolwerine ataca a Deadpool
    if regenerate:
        print("Wolverine se esta regenerando depues de recibir un golpe critico")
        regenerate = False
    elif random.random() > 0.25:
        wolverine_damage = random.randint(10,120)
        print(f'Wolwerine ataca y causa {wolverine_damage} de daño.')
        if wolverine_damage > 100:
            print(f"Golpe critico!!! Wolverine ataca con su daño maximo: {wolverine_damage} Deadpool no podra atacar.")
            regenerate = True
        deadpool_health -= wolverine_damage
        
        if deadpool_health <= 0:
            print("Vida de Deadpool llego a 0")
            break
        else:
            print(f"Vida restante de Deadpool: {deadpool_health}")
    
    else:
        print("Deadpool esquiva el ataque de Wolverine!!!!")

    time.sleep(1)
    
if deadpool_health > 0:
    print(f"Deadpool GANA la batalla, con {deadpool_health} de vida restante.")
else:
    print(f"Wolverine GANA la batalla, con {wolverine_health} de vida restante.")