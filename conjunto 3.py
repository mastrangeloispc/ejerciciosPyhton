# conjunto 3

a = frozenset({1, 2, 3}) # crea un conjunto inmutable, como las tuplas
b = {3, 4, 5}
c = {1,2,3,4,5}

print(a.issubset(c)) # pregunta si a es un sub conjunto de c (True)

print(c.issuperset(a)) # si c es un super conjunto de a (si, estan todos)

print(a.isdisjoint(b)) # si son disconexos, si no comparten nada


