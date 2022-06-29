'''
Ejercicio 3

Hacer un programa que pida una caracter y diga si es
una vocal o no
'''

l = input('Ingrese una letra ')
l = l.lower() # lo pasa a minuscula
# upper lo pasa a mayuscula


if l == 'a' or l == 'e' or l =='i' or l =='o' or l =='u':
    print(f'{l} es una vocal')
else:
    print(f'{l} no es una vocal')
    