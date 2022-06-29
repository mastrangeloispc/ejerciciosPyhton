'''
Hacer un programa que pida 3 numeros y determine cual es el
mayor.
'''
n1 = int(input('Numero 1 '))
n2 = int(input('Numero 2 '))
n3 = int(input('Numero 3 '))

if n1 > n2 and n1 > n3:
    print(f'{n1} es el mayor')
elif n2 > n1 and n2 > n3:
    print(f'{n2} es el mayor')
elif n3 > n1 and n3 > n2:
    print(f'{n3} es el mayor')
    
else:
    print('Son todos iguales')
    
    
    
    
    

    



