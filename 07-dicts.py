### Dictionaries ###
# Es una estructura de datos, de tipo clave-valor

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Greg", "Apellido":"Carrillo", "Edad":35, 1:"Python"}

my_dict = {
    "Nombre":"Greg",
    "Apellido":"Carrillo",
    "Edad":35,
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.77
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict)

print(my_dict[1])

my_dict["Calle"] = "Sta Margarita"
print(my_dict)

del my_dict["Calle"] # forma de eliminar un elemento del diccionario
print(my_dict)

print("Carrillo" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list)) # crea un diccionario con claves sin valor, no es habitual
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, "Gregorio")
print(my_new_dict)
