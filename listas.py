# listas

lista1 = [1,2,4,5, 'Roberto']
lista2 = [6,7,8,4,6,7,8,3,1,5,1]*2 # el *2 duplica la lista

lista3 = lista1+lista2 #concatena listas

print(lista3)

print('Roberto' in lista1) # busca un elemento y True si esta
print({lista1.index('Roberto')}) # dice en que indice esta
print({lista3.count(1)}) # cuantos 1 hay en la lista
lista1.append(6) # agrega un elemento al final
lista1.insert(2,3) # agrega el elemento 3 en el indice 2
lista3.pop() # elimina ultimo elemento
lista3.pop(3) # elimina el inice 3
lista3.remove(5) # elimina el valor 5 (el primero que encuentre
lista3.clear # elimina el tontenido de la lista
lista3.reverse # invierte la lista
lista2.sort() # ordena ascendente (numeros)
lista2.sort(reverse=True) # ordena descendente
print(lista2)
print(lista3)




