import time
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# Devuelve el epoch, tiempo de partida desde 1970 a la actualidad en segundos
print(time.time())

# Fecha de referencia con el gmt, timezone aware
reference = datetime.now(timezone.utc)
print(reference)

# fecha naive, sin zona horaria
naive = datetime.now()
print(naive)

# Transformar a la zona horaria del pais, viene con el gmt
mexico = datetime.now(ZoneInfo("America/Mexico_City")) # La info sale de la base de datos IANA Code
print(mexico)

argentina = datetime.now(ZoneInfo("America/Buenos_aires")) # La info sale de la base de datos IANA Code
print(argentina)
