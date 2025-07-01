from boltons.iterutils import backoff, backoff_iter
import time

# Da una coleccion de numeros que van aumentando exponencialmente,
# normalmente usados para reintentar una operacion fallida

values =  backoff(1.0,1000.0, jitter=False)
print('Backoff:', values)

#backoff_iter es un iterador que te da los valores de backoff
# al ser un iterador, puede generar una coleccion infinita de valores

# frenar con ctrl+c
"""for v in backoff_iter(1.0, 1000.0, count="repeat"):
    print(f'Esperando {v} segundos')
    time.sleep(v)"""

from boltons import urlutils

mi_url = urlutils.URL("http://www.ejemplo.com:8000/")

print("URL", mi_url)
print("Host", mi_url.host)
print("URL", mi_url.port)
print("URL", mi_url.scheme)
print("URL", mi_url.path)
