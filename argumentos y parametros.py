# argumentos y parametros

def restar(num1, num2): # parametros
    return num1-num2
# con esto podemos retornar un valor sin necesidad de crear una variable extra

print(restar(10,2)) # argumentos. los pasa por posicion (10 num1, 2 num2)
print(restar(num2=2, num1=10)) # pasa los argumentos por nombre


'''
llama a la funcion (restar), le asigna el valor a la variable correspondiente
(10 num1 y 2 num2) y realiza la operacion de la funcion (restar)

Esto se llama "paso de argumentos".

Cuando se invoca directamente el nombre de la funcion para
pasarle valores

'''
