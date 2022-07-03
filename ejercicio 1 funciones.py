'''
Ejercicio 1 funciones

Desarrollar un programa que pueda calcular el valor del tipo
de cambio de moneda ($ a dolar) y viceversa.

'''
def cambio_Pesos_Dolares(pesos):
    return pesos/120

def cambio_Dolares_Pesos(dolares):
    return dolares*120

while True:
    print('''\t.:MENU:.
1. Convertir de Pesos a Dólares
2. Covertir de Dólares a Pesos
3. Salir''')
    opcion = int(input('Digite una opción'))
                
    print()
    
    if opcion ==1:
        pesos = float(input('Digite la cantidad de pesos '))
        print(f'Dólares -> Pesos {cambio_Pesos_Dolares(pesos):.2f}')
        
    elif opcion==2:
        dolares = float(input('Digite la cantidad de Dólares '))
        print(f'Pesos -> Dólares {cambio_Dolares_Pesos(dolares):.2f}')
        
    elif opcion==3:
        break
    
    else:
        print('Error')
        
    print()
    
        
        
        
    
