"""
/*
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
 */
"""

import logging

logging.basicConfig(level=logging.DEBUG, 
                    format="%(asctime)s-[%(levelname)s]: %(message)s",
                    handlers=[logging.StreamHandler()])
                    #handlers=[logging.FileHandler(filename="25- Loggins/log.log")])




class TaskManager:

    def __init__(self) -> None:
        self.tasks = {}


    def add_task(self,name:str, description:str):
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(f"Tarea añadida: {name}")
        else:
            logging.warning(f"Se ha intentado añadir una tarea que ya existe: {name}")
        logging.debug(f"Numero de tareas: {len(self.tasks)}")
        

    def delete_task(self,name:str):
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"Se ha eliminado la tarea: {name}")
        else:
            logging.error(f"Se ha intentado eliminar una tarea que no existe: {name}")
        logging.debug(f"Numero de tareas: {len(self.tasks)}")

    def list_task(self):
        if self.tasks:
            for name,description in self.tasks.items():
                print(f"{name}: {description}")
            logging.info("Imprimiendo tareas")
        else:
            logging.info(f"No hay tareas para mostrar")

task_manager = TaskManager()
task_manager.add_task("Pan","Comprar 1kg de pan")
task_manager.add_task("Python", "Estudiar Python")
task_manager.list_task()