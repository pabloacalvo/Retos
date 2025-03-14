import itertools
import toolz


transacciones = [4, 5, 6, 7, 3, 1, 1, 4, 5]

# Usar toolz para agrupar, no es necesario ordenar
grupos_toolz = toolz.itertoolz.groupby(lambda x: x, transacciones)

for grupo, values in grupos_toolz.items():
    print(f"Grupo {grupo}: {values}")

print("-------------------")


# Usar itertools para agrupar
# Primero hay que ordenar
transacciones_ordenadas = sorted(transacciones)
grupos_itertools = itertools.groupby(transacciones_ordenadas)

for grupo, values in grupos_itertools:
    print(f"{grupo = }: {list(values)}")


