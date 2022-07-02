# conjuntos 2
''' si se crea un conjunto que no estará vacio, se puede
poner de entrada, sin el set
porquye se le ponen comas, en los diccionarios se usan :
entonces py sabe que es un conjunto
'''

a = {1, 2, 3}
b = {3, 2, 1 , 8, 4, 2}

''' Para unir dos conjunto, a diferencia de las listas
que seria c=a+b, acá no es asi la cosa'''

print(a == b) # se fija si el conjunto a es igual al b. 

print(len(a)) # cuantos elementos

union = a | b # esto une los conjuntos a y b bajo el c. Se pone con altgr+1

inter = a & b # interseccion de dos conjuntos (los que se repiten)

dife = a - b # los diferentes. Los que estan en el a pero no en el b

difesim = a ^ b # diferencia simetric

print(union)
print(inter)
print(dife)
print(difesim)


