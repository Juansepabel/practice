

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]
lista4 = [1,2,3,4,5,6]

a, *b, c = lista4
listaj = [*lista1, *lista3]

print (a)
print (b)
print (c)
print (listaj)

a = [*"python"]
print (a)

diccionario1 = {"A":1, "B":2}
diccionario2 = {"C":3, "D":4}
diccionario3 = {"E":5, "F":6, "G":7}

diccionarioj = {**diccionario1, **diccionario2}
print(diccionarioj)

#for anidado
x = [1,2]
y = [4,5]
for i in x:
    for j in y:
        print (i,j)


lista = []
for i in range(5):
    lista.append([])
    for j in range(5):
        lista[i].append(j)
print (lista)

listaA = [[j for j in range(6)]for i in range(6)]
print(listaA)

listaB = list(range(10))
print (listaB)


lista_de_listas = [[1,2,3],[4,5,6],[7,8,9]]
numeros_impares = []
for lista_interna in lista_de_listas:
    for elemento in lista_interna:
        if elemento%2 != 0:
            numeros_impares.append(elemento)
print(numeros_impares)

numeros_pares = [elemento for lista_interna in lista_de_listas for elemento in lista_interna if elemento%2 == 0]
print(numeros_pares)

