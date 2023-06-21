### Modules ###
# es un lugar donde tenemos codigo de otros ficheros

import my_module # importa el fichero completo

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola python")

from my_module import sumValue, printValue # importa codigo especifico del fichero

sumValue(5, 3, 1)
printValue("Hola Python")

import math # modulos del sistema

print(math.pi)
print(math.pow(2, 8))
