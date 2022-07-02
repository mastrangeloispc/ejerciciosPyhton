# colas

'''
son una estructura de datos de tipo fifo
first input
first output
el primero en entrar, es el primero en salir
como las pilas

Como una cola en un banco, van creciendo de atras hacia adelante
y se van yendo de adelante hacia atras

en otros sitios importan el modulo collections
from collections_import deque
o con pop left

pero esto es lo mismo y dice Ale que es mejor. Asi que le doy


'''

cola = ['Juan','Pepe','Mario','Roberto']

cola.append('Romina') # agrega al final
cola.append('Susana') # agrega al final

# como hacemos para sacar al primero que llego a la cola?

n= cola.pop(0) # asi saca el primero, no el ultimo y lo guarda en n

print(f'Están atendiendo a {n}')





print(cola)