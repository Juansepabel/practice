#funciones
def nombre_funcion(num1, num2):
    return num1 + num2
print (nombre_funcion(5, 8))

#lambdas
funcion_lambda = lambda x: x * 2
print (funcion_lambda(6))
print (f"el resultado de la funcion lambda es: {funcion_lambda(4)}")

lista1 = (1,2,3,4,5,6,7,8,9)
def numeros_pares(numero):
    if numero%2 == 0:
        return True    
#filter()
print (list(filter(numeros_pares, lista1)))
print (list(map(lambda x: x%2 == 0, lista1)))

lista2 = [funcion_lambda(x) for x in lista1 if x%2 == 0]
print (lista2)


