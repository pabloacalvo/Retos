import arrow

# Se crea un objeto Arrow con la fecha y hora actual
ahora = arrow.now()
print(f'Fecha y hora actual: {ahora}')

ahora_utc = arrow.utcnow()
print(f'Fecha y ahora actual UTC: {ahora_utc}')

# Objeto Arrow con fecha y hora especifica
especifico = arrow.get("2023-05-11 12:30:45", "YYYY-MM-DD HH:mm:ss")
print(f'Fecha y hora especifica: {especifico}')

# Tiempo que paso desde una fecha especifica en español
print(f"Desde {especifico} como fucha humanizada: '{especifico.humanize(locale='es')}")