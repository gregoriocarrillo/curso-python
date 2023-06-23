### Dates ###

from datetime import datetime

hoy = datetime.now() # se define variable con el modulo y la funcion interna now, variable definida por el modulo datetime

def imprime_fecha(fecha): # date como parametro
    print(fecha.year)
    print(fecha.month)
    print(fecha.day)
    print(fecha.hour)
    print(fecha.minute)
    print(fecha.second)
    print(fecha.timestamp())

imprime_fecha(hoy) # se llama a la funcion y como parametro la variable fecha_actual

year_2024 = datetime(2024, 1, 1) # se crea variable con una fecha definida, como minimo año, mes y dia
imprime_fecha(year_2024) # se invoca la funcion y como parametro la variable, se imprimira lo que contenga la funcion, se reusa la funcion con diferentes parametros

from datetime import time

current_time = time(13, 18, 0) # se define la hora

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today() # modulo que solo muestra la fecha, variable que se define a raiz del modulo date

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2023, 6, 23) # se puede definir la fecha

print(current_date.year)
print(current_date.month)
print(current_date.day)

# Operaciones con fechas

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.year)
print(current_date.month)
print(current_date.day)

# se pueden realizar operaciones con objetos del mismo modulo
diff = year_2024 - hoy
print(diff)

diff = year_2024.date() - current_date
print(diff)

from datetime import timedelta

init_time_delta = timedelta(200, 100, 200, weeks = 10)
end_time_delta = timedelta(300, 200, 100, weeks = 3)

print(end_time_delta - init_time_delta)
print(end_time_delta + init_time_delta)