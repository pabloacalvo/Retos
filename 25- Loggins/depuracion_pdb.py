import logging
from pathlib import Path


# Permite detener la ejecucion del programa

DEBUG = True
level = logging.DEBUG if DEBUG else logging.ERROR
root = Path(__file__).parent
logging.basicConfig(level=level, filename=f"{root}/error.log", format="%(asctime)s %(message)s")


def function_a():
    logging.info("@@@ Function A")
    breakpoint() # Forma 2
    import pdb; pdb.set_trace() # Forma 1
    number_a = 0
    number_b = 10
    return number_a, number_b

def function_b():
    logging.info("@@@ Funcion B")
    number_a = 20
    number_b = funcion_a()
    return (number_a, ) + number_b

def function_c():
    logging.info("@@ Function C")
    number_a = 50
    number_b = function_a()
    number_a += 1
    number_a += 1
    number_a += 1
    number_a += 1
    return (number_a, ) + number_b


try:
    result = function_c()
    print(result)
except Exception as err:

    logging.error("Ocurrio un error")