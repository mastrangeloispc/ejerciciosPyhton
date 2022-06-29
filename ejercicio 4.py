'''
Ejercicio 4

Hacer un programa para ingresar el radio de un circulo y
se reporte su area y la longitud de la circunferencia.

area = pi * radio al cuadrado
longitud = 2 * pi por radio
'''
radio = float(input('Ingrese el radio de la circunferencia '))

import math
math.pi

pi=math.pi

area = pi * radio **2
longitud = 2 * pi * radio

print(f'El área de la circunferencia es {area}.')
print(f'El longitud de la circunferencia es {longitud}.')

