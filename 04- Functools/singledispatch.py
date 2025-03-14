from functools import singledispatch
"""
Transforma una funcion en otra segun el tipo de dato, polimorfismo 
"""


@singledispatch
def add(a,b):
    raise NotImplementedError("Unsupported type")

@add.register(int)
def _(a, b):
    print("Type`s argument: ",type(a))
    return a + b

@add.register(list)
def _(a, b):
    print("Type`s argument: ",type(a))
    return sum(a) + sum(b)

print(add([3,4,5,6],[1,2,3,4]))

print(add(3,4))
