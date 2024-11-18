a = 1
b = 2
print (f"El valor de a es {a}")
print (f"El valor de b es {b}")


a, b = b, a
print (f"El valor de A es {a}")
print (f"El valor de B es {b}")


numero = 10
if numero > 0:
    print ("El numero es positivo")
elif numero == 0:
    print ("El numero es cero")
else:
    print ("El numero es negativo")


edad = int(input("digita tu edad: "))
if edad > 0 and edad < 100:
    print("Edad dentro del rango")
    if edad >= 18:
        print ("Eres mayor de edad")
    else:
        print ("Eres menor de edad")


letra = input("Digita un caracter: ")
print(letra)
letra = letra.lower()
print(letra)
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print ("Es una vocal")
else:
    print ("No es una vocal")


lista = ["Hola", 4, 8.4, [1, 2, 3], True]
lista2 = []
print (lista[0])
print (lista[3])
print (lista[0:3])
print (lista[-1])
# print (lista.pop())
# print (lista.pop(1))
elemento_eliminado = lista.pop()
print (lista)
print (elemento_eliminado)

numeroslista = [3, 5, 1, 2, 4]
letraslista = ["e", "a", "i", "u", "o"]
print (numeroslista)
print (letraslista)
numeroslista.sort()
copialista = letraslista.copy()
copialista.sort()
print (numeroslista)
print (letraslista)
print (copialista)
