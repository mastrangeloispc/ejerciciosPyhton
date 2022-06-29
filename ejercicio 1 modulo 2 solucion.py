''' Hacer un programa que pida 2 numero y se de cuenta
de cual de ellos es par, o si ambos lo son

%	Realiza un módulo entre los operandos	16 % 3 = 1

'''

num1 = int(input('Numero 1 '))
num2 = int(input('Numero 2 '))

if num1%2==0 and num2%2==0:
    print('Ambos son pares')
elif num1%2==0 and num2%2!=0:
    print(f'{num1} es par')
elif num1%2!=0 and num2%2==0:
    print(f'{num2} es par')
else:
    print('Ambos son impares')
    