import itertools

"""
 Crea un iterador que repite indefinidamente los elementos de un iterable. 
 Es útil cuando necesitas un bucle infinito sobre una secuencia de elementos.
"""

def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element



data = ['A', 'B', 'C']
cycle_iter = itertools.cycle(data)

for i in range(10):
    print(next(cycle_iter))

