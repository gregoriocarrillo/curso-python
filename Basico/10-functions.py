### Functions ###

def my_function ():
    print("Esto es una funcion")

my_function ()

def sum_two_values (first_value, second_value):
    print(first_value + second_value)

sum_two_values (5, 7)
sum_two_values ("5", "7")
sum_two_values (5.1, 7.2)

# usamos return para que retorne los valores que le pasamos a la funcion
def sum_two_values_with_return (first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name("Greg", "Carrillo")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Greg", "Carrillo")
print_name_with_default("Greg", "Carrillo", "roswel47")

def print_texts(*text):
    print(text)

print_texts("Hola")
print_texts("Hola", "Python", "roswel47")

def print_texts(*texts):
    for text in texts:
        print(text)

print_texts("Hola")
print_texts("Hola", "Python", "roswel47")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "roswel47")