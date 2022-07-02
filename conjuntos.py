# Conjuntos

''' Son grupos de datos desordenados, en donde no pueden
haber duplicados. Solo existen valores unicos. Si se repiten
no les da bola

los conjuntos y los diccionarios tienen el mismo tipo
de llaves

lo creo en dos etapas, porque sino para python eso seria
un diccionario

no pueden haber otro tipo de colecciones (listas o tuplas)

'''

conjunto = set() # crea un conjunto vacio

conjunto = {1,2,3, "hola", 4, 6}
conjunto.add(5) # agrega el 5, pero no lo pone al final
conjunto.add('chau') # lo pone donde se le canta el culo
conjunto.discard(4) # elimina el valor 4
''' conjunto.clear() # borra todo '''

print(conjunto)
print(3 in conjunto) # busca el 3 en conjunto
print(3 not in conjunto) # se fija si NO esta




