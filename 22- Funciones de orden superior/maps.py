""" La funcion map aplica una funcion sobre todos los elemtnos y como resultado
    devuelve un iterable de tipo map.
    MAP(FUNCION, ITERABLE1,ITERABLE2,ITERABLE3,...)
"""
"""
    La función map() se utiliza mucho junto a expresiones lambda ya que permite 
    ahorrarnos el esfuerzo de crear bucles for.
"""

lista = [1,2,3,4,5]


def multiplica_nums(numero):
    return numero * 2

def sumar_num(a,b,c):
    return a + c + b

# Objeto map
print(map(multiplica_nums,lista))

# Casteo de map a lista
print(list(map(multiplica_nums,lista)))

# La funcion str convierte los elementos de la lista a string
print("-".join(map(str,lista)))

# Usando lambda
print(list(map(lambda x: x * 2, lista)))

# Multiples iterables, suma primer elemento de cada iterable
print(list(map(sumar_num,[1,2,3,4],[1,2,3,4],[1,2,3,4])))

