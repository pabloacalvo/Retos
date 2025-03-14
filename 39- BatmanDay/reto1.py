""" 
/*
 * EJERCICIO:
 * Cada año se celebra el Batman Day durante la tercera semana de septiembre...
 * ¡Y este año cumple 85 años! Te propongo un reto doble:
 *
 * RETO 1:
 * Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta
 * su 100 aniversario.
 *
"""

# Reto 1
import datetime
from datetime import timedelta
import calendar

YEAR_OF_CREATION = 1939
ANNIVERSARY_YEAR = YEAR_OF_CREATION + 85
batman_day_anniversary_dates = []


while ANNIVERSARY_YEAR <= YEAR_OF_CREATION + 100:
    # Primer semana de septiembre
    first_day = datetime.date(ANNIVERSARY_YEAR, 9, 1)
    # Valido que dia cae, 0= lunes 6=domingo
    # Si de 0, a 5 es decir lunes a sabado, le resto para sabar cuanto falta para llegar al sabado
    # Si es mayor a 5, es decir, domingo le resto a 12 porque ya calculo cuantos dias faltan para el proximo sabado
    # Por ejemplo 12 - 6 = 6 osea faltan 6 dias para el proximo sabado siendo domingo;
    first_saturday = 5 - first_day.weekday() if first_day.weekday() <= 5 else 12 - first_day.weekday()
    # Calculo el tercer sabado, para eso le sumo al primer dia de septiembre un timedelta de dias del primer sabado + 14 dias
    # Uso timedelta para hacer operaciones con fechas.
    third_saturday = first_day + timedelta(days=first_saturday + 14)
    # Guardamos año calculado, numero de año de aniversario y fecha que cae
    batman_day_anniversary_dates.append(
        (
        ANNIVERSARY_YEAR, 
        ANNIVERSARY_YEAR - YEAR_OF_CREATION,
        third_saturday.strftime("%d/%m/%Y")
        )
    )

    ANNIVERSARY_YEAR += 1

for year,anniversary, batman_day in batman_day_anniversary_dates:
    print(f"Batman day {year} - {anniversary} aniversario: {batman_day}")




