### Loops ###

# While

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
        print("Mi condicion es 15")
        break
    
    print(my_condition)

print ("La ejecucion continua")