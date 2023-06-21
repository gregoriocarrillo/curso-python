## Operadores Aritmeticos

print(4 + 3)
print(4 - 3)
print(4 * 3)
print(4 / 3)
print(10 % 3) # el resto es el numero que sobra de la operacion
print(10 // 3) # da el resultado el numero entero de la division
print(2 ** 3)

# No todos los operadores funcionan con cadenas de textos
print("Hola " + "Python") # concatena cadenas de textos
print("Hola " * 2) # repite la cadena de texto las veces que se indique

## Operadores Comparativos
print(3 > 4) #False
print(3 < 4) #True
print(3 <= 4) #True
print(3 >= 4) #False
print(3 == 4) #False
print(3 != 4) #True

print("Hola" > "Python") #False
print("Hola" < "Python") #True
print("Hola" >= "Zola") #False
print("Hola" <= "Python") #True
print("Hola" == "Python") #False
print("Hola" != "Python") #True
print("aaaa" >= "AAAA") #True ordenacion alfabetica por ASCII

## Operadores Logicos
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(not (3 > 4))