'''
Llenar una lista con los numero del 1 al 10, luego modificar
los elementos de la lista multiplicandoloes por un valor
que el usuario digite
'''

lista = list(range(1,11))


print('Lista original: ')

for i in lista:
    print(i, end='-')
    
valor= int(input('\nIngrese un valor '))
''' 
indice = 0
 for i in lista:
    lista[indice] *= valor
    indice += 1
'''

# esto de abajo hace lo mismo que lo de arriba utlizando enumerate

for indice,i in enumerate(lista):
    lista[indice] *= valor
    

print(f'\nLista multiplicada por {valor}')

for i in lista:
    print(i, end='-')

