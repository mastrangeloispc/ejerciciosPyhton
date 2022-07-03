# funciones con retorno de valor

def multiplicar(num1,num2): # crea la funcion multi con dos variables
    mult = num1*num2 # las multiplica y el resultado es x
    return mult # retorna el valor

mult = multiplicar(3,4)

print(mult)

print(multiplicar(7,8)) # los variables toman los valores que se les asignan despues de llamarlas (num1 y num2)
print(multiplicar(3,9)) # y ejecutan la funcion con esos valor. En este caso, los multiplican entre si

