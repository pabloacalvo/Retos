# Objetivo un codigo mas legible y armonico al ocupar menos lineas
temps = [221, 234,340,230]
new_temps = [temp /10 for temp in temps]
print(new_temps)

#Con IF
temps_2 = [221, 234,340,-9999,230]
new_temps_2 = [temp /10 for temp in temps if temp > 0]
print(new_temps_2)

#Con IF y ELSE
temps_3 = [221, 234,340,-9999,230]
new_temps_3 = [temp / 10 if temp > 0 else 0 for temp in temps_3]
print(new_temps_3)

# Ejemplo de eliminar varios elementos
seconds = [1.23, 1.45, 1.02, 1.11]
removes = [1.45, 1.02, 1.11]

seconds = [num for num in seconds if num not in removes]



# EJERCICIOS

def get_integers(elements:list):
    integer_list = [element for element in elements if isinstance(element, int)]
    return integer_list

def get_positive_number(numbers:list):
    positive_numbers = [number for number in numbers if number > 0]
    return positive_numbers

def replace_string_for_zero(elements:list):
    interger_list = [element if isinstance(element, int) else 0 for element in elements]
    return interger_list


def sum_numbers(elements:list):
    return sum([float(element) for element in elements])

    



"""result = replace_string_for_zero([99, 'no data', 95, 94, 'no data'])
print(result)

result2 = get_positive_number([-5,3,-1,101])
print(result2)

result3 = sum_numbers(['1.2', '2.6', '3.3'])
print(result3)"""




"""
Generator expressions
Son tipos particulares de experesiones que devuelven generator iterators. La sintaxis de un Generator Expressions es casi
la misma que la una lista por compresion. Solo necesita convertir los corchetes[] en paretensis ().
"""
# Diferencia en el consumo de memoria 

import sys
# Secuencia de numeros
n = 10 **6

# Usando lista (carga en memoria)
list_of_numbers = list(range(n))
print(f"Tamaño en memoria de la lista: {sys.getsizeof(list_of_numbers)} bytes")

# Usando generador(no carga todos los elementos en memoria  a la vez)
generator_of_numbers = (x for x in range(n))
print(f"Tamaño en memoria del generador: {sys.getsizeof(generator_of_numbers)} bytes")
