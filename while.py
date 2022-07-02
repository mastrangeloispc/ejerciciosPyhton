# bucle while

''' numero indeterminado de repeticiones
mientras...


'''

import math # importa el modulo math para la raiz cuadrada

numero = int(input('Digite un numero: '))

while numero<0: # mientras numero sea menor a 0
    print('Ingrese un numero positivo')
    numero = int(input('Digite un numero: '))
    
print(f'\nLa raíz cuadrada es: {(math.sqrt(numero)):.2f}') 

'''
math.sqrt raiz cuadrada de numero
\n salto de linea

.2f dos decimales

'''
    
    



