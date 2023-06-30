### Python Package Manager ###

# pip3 install pip

import numpy

#numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
#sprint(type(numpy_array))

# pip3 list
# pip3 uninstall (libreria)
# pip3 show (libreria)

import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)