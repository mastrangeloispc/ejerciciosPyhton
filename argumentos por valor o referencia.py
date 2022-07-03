# argumentos por valor o por referencia

def doblarValor(numero):
    numero *= 2
    print(numero)
    
n = 5
doblarValor(n)

print(n)

'''
fuera de la funcion, el valor seguira siendo el mismo

las colecciones se pasan por referencia
'''
