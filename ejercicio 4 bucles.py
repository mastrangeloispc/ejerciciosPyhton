'''
Hacer un programa para sumero numero pares dentro de un rango

Ejemplo:
    Suma de numero pares del 2 al 30
    Suma = 240

'''
a = int(input('Introduzca inicio del rango '))
b = int(input('Introduzca final del rango '))
suma=0

for i in range(a, b+1): # b+1 porque el bucle llega hasta un numero anterior
    if i%2==0: # si el numero es par
        suma+=i

print(f'\nLa suma de numero pares dentro del rango es: {suma} ')




