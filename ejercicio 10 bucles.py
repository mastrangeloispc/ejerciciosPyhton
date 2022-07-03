'''
Hacer un programa que pida una cadena por teclado,
luego ponga caracteres en una lista sin repetir caracteres
'''

cadena=input('Ingrese una frase ')

lista = [] # crea una cadena vacia

for i in cadena: # recorremos caracter por caracter la cadena con un bucle for
    if i not in lista: # si el caracter x el que vamos, no esta en la lista ...
        lista.append(i) # lo agregamos a la lista
        
print(f'\nLista de caracteres sin repetir: \n{lista}')
    
    

