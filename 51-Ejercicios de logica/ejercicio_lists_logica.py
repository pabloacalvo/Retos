"""
Crea una funcion a la cual se le pase un array de numeros y un numero que sera el 
resultado de la suma de los dos valores
"""

def add_two(numbers:list, expected_result:int):
    final_list = [num for num in numbers if num < expected_result] # elimino valores superiores al resultado
    seen = set() # set con numeros vistos para evitar resultados inversos que dupliquen (8,2 y 2,8)
    for current in final_list:
        missing_value = expected_result -  current # Calculo el numero que necesito para llegar al resultado
        if missing_value in seen: # Si el valor existe dentro del set, devuelvo ambos
            yield current, missing_value 
        seen.add(current) # Si no existe lo agrego, esto va agregando elementos en la primera iteracion.
            

    


lista = [5,10,24,3,8,2,7]
generate_data = add_two(lista,10)

quantity_results = list(generate_data)

for result in quantity_results:
    print(result)

