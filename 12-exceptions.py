### Exceptions Handlings ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# try except

try:
    print(numberOne + numberTwo)
    print("Se ha ejecutado")
except:
    print("Se ha producido un error")

# try except else finally

try:
    print(numberOne + numberTwo)
    print("Se ha ejecutado")
except:
    print("Se ha producido un error")
else: # opcional
    # se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally: # opcional
    # se ejecuta siempre
    print("La ejecucion continua")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("Se ha ejecutado")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Capturar la informacion de la excepcion

try:
    print(numberOne + numberTwo)
    print("Se ha ejecutado")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)