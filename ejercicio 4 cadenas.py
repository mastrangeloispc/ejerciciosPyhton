'''
Hacer un programa donde se reemplacen todos los espacios
de una cadena por asteriscos

y ademas cada palabra
comience por mayusculas.


'''

cadena = input('Ingrese una frase: ')


cadena = cadena.replace(" ","*")
cadena = cadena.title() 

print(cadena)
