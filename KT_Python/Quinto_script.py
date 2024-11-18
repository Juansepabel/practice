#while
number = 0
while number < 10:
    number += 1
    if number == 5:
        continue
    if number == 7:
        break
    print (f"El numero actual es  {number}")
    
#try/catch
def dividir():
    try:
        numero1 = float(input("introduce el primer numero: "))
        numero2 = float(input("introduce el segundo numero: "))
        print (f"El resultado de la division es: {numero1/numero2}")
    except ValueError:
        print("hubo un error en la ejecucion")
    except ZeroDivisionError:
        print("No es posible dividir entre 0")
    finally:
        print("Ejecucion de division finalizada")
dividir()


