# ejercicio 3 colecciones

'''
Escriba un programa donde cree una lista con los siguientes
personajes del Señor de los anillos

Nombre: Aragon
Clase: Guerrero
Raza Dunadan del norte

Nombre: Legolas
Clase: Arquero
Raza: Elfo Sindar

Nombre: Gandald
Clase: Mago
Raza: Istar

'''

personajes = []

p = {'Nombre':'Aragorn', 'Clase':'Guerrero', 'Raza':'Dunadan del Norte'}
personajes.append(p) # agrega p a la lista

p = {'Nombre':'Legolas', 'Clase':'Arquero', 'Raza':'Elfo Sindar'}
personajes.append(p)
# no se pone otra variable, porque ya fue agregada a la lista

p = {'Nombre':'Gandalf', 'Clase':'Mago', 'Raza':'Istar'}
personajes.append(p)

print(personajes)

