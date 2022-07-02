# instruccion continue y break
# continue obvia lo que haya despues del bucle (continua)

for i in range(10):
    if i==5:
        continue # cuando i=5, continua(lo saltea)
    print(i)

for i in range(10):
    if i==5:
        break # cuando i=5, se sale del bucle 
    print(i)

print('Programa finalizado')

