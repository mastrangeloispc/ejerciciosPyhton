# ejercicio cadena mas larga solucion

cadena1 = input('Digite una cadena: ')
cadena2 = input('Digite otra cadena: ')

if len(cadena1) > len(cadena2):
    print(f'La cadena mas larga es: {cadena1}')
elif len(cadena2) > len(cadena1):
    print(f'La cadena mas larga es: {cadena2}')
else:
    print('Ambas son iguales en longitud')
    
    