## STRINGS

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

# Formato

name, surname, age = "Greg", "Carrillo", 45

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # formato con tipo de dato especifico
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #mejor forma de sustituir los valores de las variables

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)

# Division
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#Reverse
reversed_language = language[::-1]
print(reversed_language)

# Funciones del sistema
my_name = "gregorio"
print(my_name.capitalize())
print(my_name.upper())
print(my_name.count("g"))
print(my_name.isnumeric())
print(my_name.upper().isupper())
print(my_name.startswith("g"))