'''
determinar si una palabra o frase es palindroma (capicua)

oso
reconocer
anita lava la tina
'''

cadena = input('Ingrese una cadena: ')
cadena = cadena.replace(" ","")
cadena = cadena.lower()
cadena2 = cadena[::-1] # copia en cadena 2 la cadena invertida

print(cadena)

if cadena == cadena2:
    print('Es un palindromo')
else:
    print('No es un palindromo')
    
cadena = 'Hola mundo'.lower() # pasa a minuscula


