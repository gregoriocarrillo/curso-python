### Classes ###

class MyEmptyPerson:
    pass # permite declarar la clase sin contenido

print(MyEmptyPerson())

'''
class Person:
    # def __init__ (self) se usa para crear un constructor de clase, no es una funcion
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

my_person = Person("Greg", "Carrillo")
print(my_person.name)
print(my_person.surname)
print(f"{my_person.name} {my_person.surname}")
'''

'''
class Person:
    def __init__(self):
        self.name = "Greg"
        self.surname = "Carrillo"

my_person = Person()
print(f"{my_person.name} {my_person.surname}")
'''

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"

    # ahora podemos agregar funciones dentro de la clase
    def walk (self):
        print(f"{self.full_name} está caminando")

my_person = Person("Greg", "Carrillo") # el tercer parametro ya esta definido en el constructor
print(my_person.full_name) # imprime lo guardado en la variable
my_person.walk() # llama la variable y la funcion

my_other_person = Person("Greg", "Carrillo", "roswel47") # sobreescribe el tercer parametro
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de Leon (El loco de los perros)" # sobreescribe el valor de la propiedad
print(my_other_person.full_name)
