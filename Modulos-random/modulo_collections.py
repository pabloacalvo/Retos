from collections import Counter, defaultdict, deque

lista = [1,2,3,4,5,6,7,8,9,1]

contador = Counter(lista)
print(contador)

contador = Counter('Murcielago')
print(contador)

# defaultdict
# Cuando no encuentra una llave, usa la funcion que le pasamos para crear un valor por defecto

d = defaultdict(int)  # int() devuelve 0 por defecto
d['a'] += 1
print(d)  # defaultdict(<class 'int'>, {'a': 1})

from collections import namedtuple

Persona = namedtuple('Persona', ['nombre', 'edad','mail'])
p = Persona('Ana', 30,"Pabloacalvo@live.com")
print(p.nombre)
print(p.edad)
print(p.mail)

from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)