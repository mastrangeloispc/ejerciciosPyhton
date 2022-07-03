'''
Hacer un programa donde el usuario ingrese una frase,
se le devolvera la misma frase pero sin espacios en
blanco y ademas un contador de cuantos caracteres
tiene la frase (sin contar los espacios en blanco).

Ejemplo:

        Frase: Hola que tal?
        Frase final: Holaquetal?
        Nº de caracteres: 11
'''

frase = input('Ingrese una frase: ') 
frase2 =  ' ' # crea una cadena de caracter vacio
for i in frase: # recorre la frase cacter x caracter 
    if i!=' ': # comprueba si el elemento recorrido es diferente de un espacio
        frase2 += i # si es diferente lo concatenamos a frase 2

frase = frase2 # almacena frase2 en frase

print(f'\n Frase final: {frase}')
print(f'Nº de caracteres: {len(frase)}')
# n de caracteres es la longitud(len) de la frase









            