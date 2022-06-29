'''
Ejercicio 4

Construir un programa que simule el funcionamiento de una
calculadora que puede realizar 4 operaciones aritmeticas
basicas (suma, resta, multiplicacion y division). El
usuario debe especificar con el primer caracter del
nombre de la operacion

S, s - Suma
R, r - Resta
P,p, M, m - Multiplicacion
D, d - Division
'''

o = str(input('Calculadora. ¿Que operacion (s, r, m, d)?'))
o = o.lower()
if o=='p':
    o='m'

n1 = float(input('Ingrese el numero 1 '))
n2 = float(input('Ingrese el numero 2 '))

if o=='s':
    print(f'{n1} + {n2} = {n1+n2}')
elif o=='r':
    print(f'{n1} - {n2} = {n1-n2}')
elif o=='m':
    print(f'{n1} X {n2} = {n1*n2}')
elif o=='d':
    print(f'{n1} / {n2} = {n1/n2}')
    
    
    
