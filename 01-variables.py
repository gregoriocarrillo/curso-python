# Variables
# Se deben nombrar en minusculas y en forma snake case usando _ para separar palabras

my_string_variable = "Variable de string"
print(my_string_variable)
print(type(my_string_variable))

my_int_variable = 10
print(my_int_variable)
print(type(my_int_variable))

my_bool_variable = True
print(my_bool_variable)
print(type(my_bool_variable))

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenacion de variables
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de: ", my_bool_variable)

# Funciones del sistema
print(len(my_string_variable)) # len() indica la longitud de caracteres de la variable

# Variables en una sola linea
name, surname, alias, age = "Gregorio", "Carrillo", "gregcarrillo", 45
print(name, surname, alias, age)

# Inputs
'''
name = input("¿Cual es tu nombre? ")
age = input("¿Que edad tienes? ")

print(name)
print(age)
'''

# Cambiar su tipo
name = 45
age = "Gregorio"
print(name)
print(age)

