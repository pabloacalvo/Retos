from functools import reduce

"""
Retorno un nuevo partial object que cuando sea llamado se comportara
como func llamado con los argumentos pasados previamente
Puede recibir como parametro el valor inicial de 'acumulador'
"""

def add(acumulador, value):
    result = acumulador + value
    print(f"{acumulador = }, {value = }, result ={result}")
    return result

data_list = [1,2,3,4,5,6,7]
result = reduce(add,data_list,10)
print(result)