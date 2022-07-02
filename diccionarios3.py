# diccionarios 3

juve = {10:'Paulo Dybala', 11:'Douglas Costa', 7:'Cristiano Ronaldo'}

print(juve[10]) # muestra la clave 10

# print(juve[6]) # da key error 6, porque no esta

print(juve.get(6, 'No existe'))
''' cuando no encuentra la clave,
entonces pone el mensaje no existe '''

print(10 in juve) # se fija si la clave 10 esta en el diccionario

print(juve.keys()) #solo muestra las claves

print(juve.values())  # muestra solo los valores

print(juve.items()) # muestra clave y valor en tuplas. util para bucles

juve.clear() # limpia diccionario







 