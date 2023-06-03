## Lists, es una estructura, un conjnuto de datos

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [45, 1.77, "Greg", "Carrillo"]

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count("Greg"))
print(my_list.count(30))
#print(my_other_list[4]) fuera de rango
#print(my_other_list[-5]) fuera de rango

age, height, name, surname = my_other_list # se desempaquetan cada elemento en una variable
print(name) # imprime el elemento que corrresponde

print(my_list + my_other_list) #concatenando listas

my_other_list.append("gcmphoto")
print(my_other_list) # incluye un elemento al final

my_other_list.insert(1, "Verde")
print(my_other_list) # inserta un elemento en la posicion indicada

my_other_list[1] = "Rojo" # cambia el valor del elemento en el indice indicado
print(my_other_list)

my_other_list.remove("Rojo")
print(my_other_list) # elimina un elemento conocido, sin importar su ubicacion

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list) # elimina el ultimo

my_pop_element = my_list.pop(2) #elimina el elemento de la posicion pero lo guarda en otra variable
print(my_pop_element)
print(my_list)

del my_list[2] #elimina elemento por indice
print(my_list)

my_new_list = my_list.copy() #copia el contenido en otra lista

my_list.clear() # limpia la lista
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])

my_list = "Hola Mundo"
print(my_list)
print(type(my_list))