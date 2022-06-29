'''
Hacer un programa qye simule un cajero automatico con un
saldo inical de $ 1.000 y tendra el siguiente menu de
opciones:

1- Ingresar dinero en la cuenta
2- Retirar dinero de la cuenta
3- Mostrar el dinero disponible
4- Salir
'''

print('Bienvenido a Banco Garca')
print('Seleccione una opcion:')
print('                      1. Ingresar dinero')
print('                      2. Retirar dinero')
print('                      3. Ver saldo')
print('                      4. Salir')

saldo=int(1000)
op=int(input())
if op==1:
    ing=float(input('Ingrese la cantidad dinero a depositar '))
    saldo+=ing
    print(f'Su saldo es de $ {saldo}')
elif op==2:
    ext=float(input('Ingrese la cantidad dinero a retirar '))
    if ext>saldo:
        print('Fondos insuficientes')
    else:
        saldo-=ext
        print(f'Su saldo es de $ {saldo}')
        
elif op==3:
    print(f'Su saldo es de $ {saldo}')
elif op==4:
    print('Chau')
else:
    print('Opcion no reconocida')
    
    






    
    
