### Contitionals ###

my_condition = False

if my_condition: # es lo mismo que if my_condition == True
    print("Se ejecuta la condicion del if")

my_condition = 5 * 5

if my_condition == 11: # si la condicion es True se ejecuta el print interno
    print("Se ejecuta la condicion del segundo if")

# if else
if my_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")

# if else con dos parametros en la condicion
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

# is elif else cuando se introducen dos condiciones
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25 ")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecucion continua")

my_string = "my cadena de texto"

if my_string:
    print("mi cadena de texto es vacia")

my_other_string = ""

if not my_other_string:
    print("mi cadena de texto no es vacia")
