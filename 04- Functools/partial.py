from functools import partial

""" 
se utiliza para crear funciones parciales, lo que significa que puedes “preconfigurar” 
algunos de los argumentos de una función, creando una nueva función con una firma simplificada. 
Esto es útil cuando necesitas una versión de una función con algunos parámetros ya establecidos
"""

def aplicar_descuento(precio, descuento):
    return precio - (precio * descuento)


# Se crean versiones expecializadas de la funcion para diferentes descuentos
descuento_10 = partial(aplicar_descuento, descuento=0.10)
descuento_20 = partial(aplicar_descuento, descuento=0.20)
descuento_30 = partial(aplicar_descuento, descuento=0.30)

# Lista de precios
precios = [100,200,300,400,500]


# Aplicacion de distintos descuentos a los precios
precios_con_descuento_10 = list(map(descuento_10, precios))
precios_con_descuento_20 = list(map(descuento_20, precios))
precios_con_descuento_30 = list(map(descuento_30, precios))

# Salida
print("Precios originales:", precios)
print("Precios 10% de descuento:", precios_con_descuento_10)
print("Precios 20% de descuento:", precios_con_descuento_20)
print("Precios 30% de descuento:", precios_con_descuento_30)
