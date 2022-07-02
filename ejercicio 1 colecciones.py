# ejercicio 1 capitulo 3 colecciones

'''
Escriba un programa donde tenga una lista y que, a continuacion,
elimine los elementos repetidos. Por ultimo, mostrar la lista.
'''


lista = [1,2,3,4,56,6,87,5,4,3,1,3,56,56,4,3,2,21,4,4,45,6,3]

print(lista)

# hay que pasar la lista a conjuntos

'''
conjunto = set(lista) # trasnforma la lista en conjunto
lista = list(conjunto) # transforma el conjunto en lista
'''
lista = list(set(lista)) # hace lo mismo en un paso


print(lista)



