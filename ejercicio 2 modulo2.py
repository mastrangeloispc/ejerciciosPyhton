'''
Ejercicio 3

Hacer un programa que pida una caracter y diga si es
una vocal o no
'''

l = input('Ingrese una letra ')

if l != 'a' and l != 'e' and l !='i' and l !='o' and l !='u':
    print(f'{l} no es una vocal')
else:
    print(f'{l} es una vocal')
    