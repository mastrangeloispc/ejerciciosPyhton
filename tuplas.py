# Tuplas
''' Iguales que las listas, pero inmutables. NO se puede
eliminar, ni agregar ni modificar.
Las listas van con corchetes, esto va con parentesis.
Se le pueden poner cualquier cosa. booleanos, numeros, etc

Consumen menos memoria y son mas rapidas que las listas.

Se usan para buscar

'''

tupla=(1,2,3,'Pepe', [1,2,3,4,5,])

lista = list(tupla) # transforma una tupla en lista
tupla = tuple(tupla) # transforma una lista en tupla

print(tupla)
