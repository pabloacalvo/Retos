"""
/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */

"""
def print_call(func):
    def print_funcion():
        print(f"La funcion {func.__name__} se a llamada")
        return func
    return print_funcion

# Se crea una intancia por cada decordador que es llamado desde cada funcion
def call_counter(*args):
    print(args)
    def counter_function():
        counter_function.call_cont += 1
        print(f"La funcion {args[0].__name__} se a llamado {counter_function.call_cont} de veces")
        return args[0]

    counter_function.call_cont = 0
    return counter_function

@print_call
def funcion_one():
    pass
@print_call
def funcion_two():
    pass
@print_call
def funcion_three():
    pass

@call_counter
def print_name():
    pass



funcion_one()
funcion_two()
funcion_three()
print_name()