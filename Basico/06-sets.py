### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # inicialmente lo define como un diccionario

my_other_set = {"Greg", "Carrillo", 45, 1.77}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("gcm") # un set no es una estructura ordenada, añade el elemento en cualquier posicion
print(my_other_set) 

my_other_set.add("gcm") # un set no admite repetidos
print(my_other_set)

print("Greg" in my_other_set) # identifica si elemento existe en el set

my_other_set.remove("Greg")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set)  NameError: name 'my_other_set' is not defined

my_other_set = {"Kotlin", "Swift", "Python"}
my_set = {"Greg", "Carrillo", 45, 1.77}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.union({"Javacript", "C#"})) # los elementos no estan almacenados en ninguna variable