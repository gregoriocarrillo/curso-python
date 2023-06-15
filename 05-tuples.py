### Tuples ###
# es un conjunto de valores fijos, es inmutable

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (45, 1.77, "Greg", "Carrillo")
print(my_tuple)

my_other_tuple = (35, 60, 30)

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count(45))
print(my_tuple.index("Greg"))

#my_tuple[1] = 1.80 TypeError: 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(type(my_sum_tuple))

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple) # se reasigna su tipo, se convirtio a lista, para poder modificarla
print(type(my_tuple))

del my_tuple #del elimina el objeto, ya no existe y no lo va imprimir
#print(my_tuple) NameError: name 'my_tuple' is not defined