# funciones con retorno de valor 3
def prueba():
    return "hola", 12, [1,2,3,4] #se pueden retornar varios valores de distinto tipo (cadena, int, lista)


print(prueba()) # Se almacenan dentro de una tupla
cadena, numero, lista = prueba() # almacena dentro de variables

print(cadena)
print(numero)
print(lista)



