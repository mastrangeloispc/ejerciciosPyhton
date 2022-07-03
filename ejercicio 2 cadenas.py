'''
Hacer un programa para detectar si una frase introducida por
el usuario finaliza con el punto "." o no. Deberas imprimir
por la consola una de las siguientes opciones:
"termina con un punto" o "no termina con un punto".
'''

cadena = input('Introduzca una cadena: ')

if cadena.endswith('.'):
    print('Termina con punto')
else:
    print('No termina con punto')
    