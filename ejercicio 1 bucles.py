'''
Ejercicio 1 Bucles

Llenar una lista con los numeros del 1 al 50, luego mostrar
la lista con un bucle for, los elementos deben mostrarse
de la siguiente forma:

1-2-3-4-5-...50

'''
lista = [] # crea lista vacia

i = 1 # crea una variable iteradora

while i<= 50: # mientras i sea menor o igual a 50
    lista.append(i) # agrega i a la lista 
    i+=1 # i = i+1. Le suma uno en cada bucle 

for i in lista: # imprime la lista a traves de un bucle
    print(i,end='-') #los pone en el mismo renglon separados con -
    

