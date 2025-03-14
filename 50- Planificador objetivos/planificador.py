""" 
/*
 * EJERCICIO:
 * El nuevo año está a punto de comenzar...
 * ¡Voy a ayudarte a planificar tus propósitos de nuevo año!
 *
 * Programa un gestor de objetivos con las siguientes características:
 * - Permite añadir objetivos (máximo 10)
 * - Calcular el plan detallado
 * - Guardar la planificación
 *
 * Cada entrada de un objetivo está formado por (con un ejemplo):
 * - Meta: Leer libros
 * - Cantidad: 12
 * - Unidades: libros
 * - Plazo (en meses): 12 (máximo 12)
 *
 * El cálculo del plan detallado generará la siguiente salida:
 * - Un apartado para cada mes
 * - Un listado de objetivos calculados a cumplir en cada mes
 *   (ejemplo: si quiero leer 12 libros, dará como resultado
 *   uno al mes)
 * - Cada objetivo debe poseer su nombre, la cantidad de
 *   unidades a completar en cada mes y su total. Por ejemplo:
 *
 *   Enero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   [ ] 2. Estudiar Git (1 curso/mes). Total: 1.
 *   Febrero:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *   ...
 *   Diciembre:
 *   [ ] 1. Leer libros (1 libro/mes). Total: 12.
 *
 * - Si la duración es menor a un año, finalizará en el mes
 *   correspondiente.
 *
 * Por último, el cálculo detallado debe poder exportarse a .txt
 * (No subir el fichero)
 */
"""
import os

MONTHS = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

class Goal:
    def __init__(self,goal_name:str,amount:int,units:str,limit:int):
        self.goal_name = goal_name
        self.amount = amount
        self.units = units
        self.limit = limit

class GoalMonth(Goal):
    def __init__(self,name):
        super(self.goal_name,self.amount,self.units,self.limit)


def show_menu():
    print("\n Planificador de objetivos")
    print("1- Añadir objetivo")
    print("2- Cacular plan detallado")
    print("3- Guardar planificacion")
    print("4- Salir")


def request_goal()->Goal:
    goal_name = input("Meta: ")
    while True:
        try:
            amount = int(input("Cantidad: "))
            if amount <= 0:
                print("La cantidad debe ser mayor a 0")
                continue
            break
        except:
            print("Introduce un numero entero valido")
    units = input("Unidades: ")
    while True:
        try:
            limit = int(input("Plazos en meses: "))
            if amount <= 0 or limit > 12:
                print("La cantidad debe ser mayor a 0")
                continue
            break           
        except:
            print("Introduce un numero entre 1 y 12")
    return Goal(goal_name,amount,units,limit)


def calculate_detailed_plan(goals:list)->dict:
    plan = {month: [] for month in range(1,len(MONTHS) + 1)}
    for goal in goals:
        month_amount = goal.amount / goal.limit
        for month in range(1,goal.limit + 1):
            plan[month].append(Goal(goal.goal_name, month_amount, goal.units, goal.amount))

    return plan

def show_detailed_plan(plan:dict):
    for month in range(1,len(MONTHS) + 1):
        if not plan[month]:
            break
        else:
            print(f"{MONTHS[month - 1]}: ")
            for index,goal in enumerate(plan[month], start=1):
                print(f"[ ] {index}. {goal.goal_name} ({goal.amount} {goal.units}/mes). Total: {goal.limit}.")


def save_detailed_plan(plan:dict):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plan.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Plan detallado:\n")

        for month in range(1,len(MONTHS) + 1):
            if not plan[month]:
                break
            else:
                file.write(f"{MONTHS[month - 1]}: \n")
                for index,goal in enumerate(plan[month], start=1):
                    file.write(f"[ ] {index}. {goal.goal_name} ({goal.amount} {goal.units}/mes). Total: {goal.limit}.\n")
    print(f"Plan guardado con exito en {file_path}")


goals = []

while True:
    show_menu()
    option = input("Elige una opcion...")
    match option:
        case "1":
            if len(goals) > 10:
                print("Has alcanzado el numero maximo de obejtivos")
            else:
                goal = request_goal()
                goals.append(goal)
                print("Objetivo añadido")
        case "2":
            if len(goals) == 0:
                print("No hay objetivos añadidos")
            else:
                plan = calculate_detailed_plan(goals)
                show_detailed_plan(plan)
        case "3":
            if len(goals) == 0:
                print("No hay objetivos añadidos")
            else:
                plan = calculate_detailed_plan(goals)
                save_detailed_plan(plan)
        case "4":
            print("Has salido del programa")
            break
        case _:
            print("Elige una opcion en 1 y 4")

