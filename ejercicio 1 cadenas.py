'''
Hacer un programa donde se debera imprimir por consola
la palabra con mas caracteres de dos palabras dadas.

En el caso de que ambas tengan la misma cantidad de
caracteres, deberas mostrar el mensaje "son iguales".
'''
 
a=input('Ingrese la primer palabra: ')
b=input('Ingrese la segunda palabra: ')
 
ac=len(a)
bc=len(b)
print(f'La palabra {a} tiene {ac} caracteres.')
print(f'La palabra {b} tiene {bc} caracteres.')

if ac>bc:
    print(f'{a} es mas larga que {b}')
elif ac<bc:
    print(f'{b} es mas larga que {a}')
else:
    print('Tienen la misma extension')
    
    
 