lista1 = [1,3,4,6,8,5]

#tupla -> listas no mutables
tupla1 =tuple()
tupla2 = (4, "hola", 3.2, (1,2,3), 6, 4, 4, 1 )
print (tupla2)
print (tupla2.index(3.2))
print (tupla2.count (4))
print (len("hola"))
lista2 = list(tupla2)
print (lista2)

#conjuntos => listas sin elementos duplicados
conjunto = {3,2,6,1,4,5,1}
print (conjunto)
conjunto.add (7)
print (conjunto)
conjunto.discard(1)
print (conjunto)
conjunto.clear
print (conjunto)
print (2 in conjunto)
print (8 not in conjunto)

#doccionarios = listas mapeadas ()
diccionario = {"3":"tres","1":"uno","4":"cuatro", "2":2}
print (diccionario)
print (diccionario["1"])
del (diccionario["3"])
print (diccionario)

lista3 = (1,2,3,4,5,6,7,8,9)
for var in lista3:
    print (var)

lista4 = []
for x in lista3:
    lista4.append(x * 2)
print (lista4)

lista5 = [x+2 for x in lista4 if x%2 == 0]
print (lista4)
print (lista5)

