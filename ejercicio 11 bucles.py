'''
HAcer un programa que simule una agenda de contactos.
Crear un diccionario donde la clave sea el nombre del
usuario y el valor sea el telefono. El programa tendra
el siguiente menu de opciones:

1. Nuevo contacto
2. Borrar contacto
3. Ver contacto existentes
4. Salir
'''

agenda = {} # crea como diccionario vacio

while True:
    print('\t.:MENU:.')
    print('1. Nuevo Contacto')
    print('2. Borrar Contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion=int(input(f'\nDigite una Opción del Menú '))
    
    print()
    
    if opcion== 1:
        nombre = input('Nombre del contacto: ')
        telefono = input('Numero de teléfono: ')
        
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado correctamente')
        else:
            print('Ese nombre de contacto ya existe')
            
    elif opcion==2:
        nombre = input('Nombre del contacto a borrar: ')
        
        if nombre in agenda:
            del(agenda[nombre])
            print('Contacto eliminado')
        else:
            print('Ese contacto no existe')
            
    elif opcion==3:
        print('Agenda de Contactos: ')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Teléfono: {valor}')
            
    elif opcion==4:
        print('Chau')
        break
    
    else:
        print('Opción incorrecta')
        
    print()
        
            
            
        
        
    
           
    
    