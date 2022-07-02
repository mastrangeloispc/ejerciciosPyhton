'''
Pide numeros y metelos en una lista, cuando el usuario
ponga 0 ya dejaremos de insertar. Por ultimo, muestra
los numeros ordenados de manor a mayor
'''
lista = [] # crea una lista vacia

salir = False # crea una variable booleana

while not salir:
    '''
    para que entre en el bucle while lo niega'''
    numero= int(input('Ingrese un valor para la lista '))
    if numero==0:
        salir = True # si el numero es 0, salir se convierte en true
    else:
        lista.append(numero)

lista.sort() #ordena la lista de menor a mayor

print(f'Lista ordenanda: \n{lista}')



