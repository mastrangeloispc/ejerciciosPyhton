'''
hacer un programa donde se cuente cada una de las vocales
en una cadena. Mostrar el conteo de las apariciones
de cada vocal.
'''

m = input('Decime algo: ')
m=m.lower()

ma=m.count('a')
me=m.count('e')
mi=m.count('i')
mo=m.count('o')
mu=m.count('u')

total=ma+me+mi+mo+mu
print(f'La frase tiene {total} vocales.')
print(f'Tiene {ma} letras a.')
print(f'Tiene {me} letras e.')
print(f'Tiene {mi} letras i.')
print(f'Tiene {mo} letras o.')
print(f'Tiene {mu} letras u.')





