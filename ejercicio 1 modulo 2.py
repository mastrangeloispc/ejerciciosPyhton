''' Hacer un programa que pida 2 numero y se de cuenta
de cual de ellos es par, o si ambos lo son

%	Realiza un módulo entre los operandos	16 % 3 = 1

'''



num1 = int(input('Numero 1 '))
num2 = int(input('Numero 2 '))

if num1%2 == 0:
    res1 = 'par'
else:
    res1 = 'impar'

if num2%2 == 0:
    res2 = 'par'
else:
    res2 = 'impar'

print(f'El número {num1} es {res1}')
print(f'El número {num2} es {res2}')

if res1=='par' and res2=='par':
    print('Ambos son pares')
    if res1=='par' or res2=='par':
        print('Hay un numero par')
else:
    print('No hay ningun par')
    

    
    

