# ejercicio 2 colecciones

'''
Escriba un programa que tenga dos listas y que, a continuacion, cree las
siguientes listas (en las que no debe haber repeticiones):

- Lista de palabras que aparecen en las dos listas
- Lista de palabras que aparecen en la primera lista, pero no en la segunda
- Lista de palabras que aparecen en la segunda lista, pero no en la primera
- Lista de palabras que aparecen en ambas listas

'''
lista1 = [1,2,3,4,56,6,87,5,4,3,1,3,56,56,4,3,2,21,4,4,45,6,3]
lista2 = [1,23,4,33,54,56,54,234,67,2,3,54,67,8,89]


# los cambia a conjuntos y eso ya quita los repetidos

a = set(lista1)
b = set(lista2)

union = list(a | b) # une los conjuntos y los pasa a lista
soloA = list(a - b) # pone los elementos que estan solo en a y lo pasa a lista
soloB = list(b - a) # viceversa
inter = list(a & b) # interseccion de ambas listas

print(f'Union {union}')
print(f'Solo A {soloA}')
print(f'Solo B {soloB}')
print(f'Ambas {inter}')





