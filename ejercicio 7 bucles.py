'''
realizar un juego para adivinar un numero. Para ello
generar un numero aleatorio entre el 0-100 y luego
ir pidiendo numeros indicando "es mayor" o "es menor",
segun corresponda respecto a n. El proceso termina
cuando el usuario acierta. Mostrar el numero de intentos
'''



import random

azar = random.randint(0, 100)

print('\t.:Juego adivina el número de 0 al 100:.')

contador=0

while True:
    numero = int(input('Digite un numero: '))
    contador += 1
    if numero>azar:
        print(f'Digite un número MENOR')
    elif numero<azar:
        print(f'Digite un número MAYOR')
    else:
        print(f'Seee!!! Adivinaste, era el {azar}.')
        break
    
print(f'Te llevó {contador} intentos')

                 
    
    
           

