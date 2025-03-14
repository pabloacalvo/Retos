import datetime
from datetime import timedelta
# Crear dato fecha con tiempo
first_day = datetime.datetime(1991, 12, 1)
# Crear dato solo fecha
first_day = datetime.date(1991, 12, 1)
# sumar fecha
first_day += timedelta(days=1)
print(first_day)




seconds = [1.23, 1.45, 1.02, 1.11]
removes = [1.45, 1.02, 1.11]

seconds = [num for num in seconds if num not in removes]

print(seconds)

