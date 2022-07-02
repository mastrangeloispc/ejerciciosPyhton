# pilas

''' stacks. En python no existen, pero se pueden simular
Como en una pila de libros, se agregan y quitan las cosas por
el final

por lo general, cuando se saca un elemento de una pila, es
para hacer algo con el

con pop, queda.
'''

pila = [1,2,3]

pila.append(4) # agrega elementos por el final

print(pila)

n = pila.pop() # quita el elemento del final y lo guarda en n
print(f'Sacando el elemento {n}')

print(pila)

