# argumentos por valor o referencia.
# por referencia (colecciones)

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *=2
        
n = [5,10,15,20]
doblar_valores(n)

print(n)


''' ¿cuales por valor?
variables (enteros, flotantes, cadenas, booleanos)
¿cuales por referencia?
colecciones (listas, tuplas, conjuntos, diccionarios)
'''
