### Loops ###

# While, se repite varias veces en funcion de una condicion

my_condition = 0

while my_condition < 10:
    print(my_condition) # aqui va a ejecutar el bucle infinitamente
    my_condition += 2 # aqui incrementa el valor y vuelve a ejecutar
else: # es opcional
    print("Mi condicion es mayor o igual que 10")

print ("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condicion es 15") # se imprime cuando cumple la condicion
        break # detiene la ejecucion 
    
    print(my_condition)

print ("La ejecucion continua")

# For, se va a repetir tantas veces como elementos a iterar

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (45, 1.77, "Greg", "Carrillo")

for element in my_tuple:
    print(element)

my_set = {"Greg", "Carrillo", 45, 1.77}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Greg", "Apellido":"Carrillo", "Edad":35, 1:"Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break # corta el bucle y no se ejecuta el resto
    print("Se ejecuta")
else:
    print("el bucle for para diccionario ha finalizado")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue # vuelve al for y continua con el siguiente elemento
    print("Se ejecuta")
else:
    print("el bucle for para diccionario ha finalizado")