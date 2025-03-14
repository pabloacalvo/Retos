# Recibe una funcion y un iterable, y aplica la funcion a cada elemento
numbers = [1,5,2,3,4]

def multiply(n:int):
    return n * 2

print(list(map(multiply,numbers)))

# Filtra los elementos que devuelven true en la funcion
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even,numbers)))

# Sorted, ordena los elementos
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, key=lambda x: -x ))

# Reduce
from functools import reduce

# Devuelve un solo valor depues de aplicar la funcion en forma acumulativa

def sum(x,y):
    return x + y

print(reduce(sum,numbers))