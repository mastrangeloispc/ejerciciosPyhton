''' Condicionales
If es Si condicional (si suece esto...)
Else es Si no (Sino...)
Elif es Else If
'''

numero = int(input('Digite un numero: '))

if numero>0:
    print('El numero es positivo')
    # Pero el 0 no es positivo ni negativo
elif numero==0:
    print('El numero es 0')
else:
    print('El numero es negativo')
    


