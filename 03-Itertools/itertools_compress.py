import random
from itertools import compress
import toolz

""" 
Se utiliza para filtrar elementos de un iterable utilizando una lista de valores booleanos como selector
"""


class GrupoUsuarios:
    def __init__(self, name, usuarios):
        self.name = name
        self.usuarios = usuarios
        self.indice = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice >= len(self.usuarios):
            raise StopIteration
        usuario = self.usuarios[self.indice]
        self.indice += 1
        return usuario
    
    def __str__(self):
        return f"El grupo {self.name} tiene {len(self.usuarios)} usuarios"
    
    def __len__(self):
        return len(self.usuarios)
    

class GeneradorNumeroAliatorio:
    def __init__(self, cantidad, minimo, maximo):
        self.cantidad =  cantidad
        self.minimo = minimo
        self.maximo = maximo
        self.generados = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.generados >= self.cantidad:
            raise StopIteration
        self.generados += 1
        generado = random.randint(self.minimo, self.maximo)
        print("Aleatorio generado: ",generado)
        return generado
    
    def __str__(self):
        return (f"Se generan {self.cantidad} numeros aleatorios entre el")
    

usuarios = [
    {"nombre":"Ed", "edad":28, "email":"edexample@gmail.com", "rol":"user"},
    {"nombre":"Bob", "edad":34, "email":"bobexample@hotmail.com", "rol":"admin"},
    {"nombre":"Charlie", "edad":21, "email":"charexample@gmai.com", "rol":"user"},
    {"nombre":"Camila", "edad":40, "email":"camexample@gmail.com", "rol":"admin"},
    {"nombre":"Mary", "edad":22, "email":"sdsxample@yahoo.com", "rol":"user"},
    {"nombre":"Dana", "edad":41, "email":"dexample@live.com", "rol":"admin"}
]


grupo_usuarios = GrupoUsuarios("Codigo Facilito", usuarios)
print(grupo_usuarios)

filter_random = GeneradorNumeroAliatorio(
    len(grupo_usuarios), minimo=0, maximo=1
)
print(filter_random)

print("-------------------")

compress_iter = compress(grupo_usuarios, filter_random)

for dato in compress_iter:
    print(dato)

# Usando groupby para mostrar usuarios por rol
grupos = toolz.groupby("rol", usuarios)

for key,value in grupos.items():
    print(f"{key=} :{value}")