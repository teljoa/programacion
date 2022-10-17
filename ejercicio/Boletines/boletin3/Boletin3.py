'''
1. Realizar un programa que lea un número entero por teclado e informe de si el número es par o impar (el cero se considera 
par).
'''

numero = int(input("Introduzca un numero:"))

if numero%2==0:
    print("El numero %s es par" % (numero))
    
else:
    print("El numero %s es impar" % (numero))

'''
2. Realizar un programa que solicite dos números por teclado e imprima en pantalla si son iguales, el primero mayor que el 
segundo o el primero más pequeño que el segundo.
'''
numero1 = int(input("Introduzca el numero:"))
numero2 = int(input("Introduzca el numero:"))

if numero1 == numero2:
    print("Ambos numeros son iguales")
    
elif numero1 > numero2:
    print("El numero %s es mayor que el numero %s" %(numero1, numero2))
    
else:
    print("El numero %s es menor que el numero %s" %(numero1, numero2))

'''
3. Realizar un programa que lea un número por teclado. El programa debe imprimir en pantalla un mensaje con “El número xx es 
múltiplo de 2” o un mensaje con “El número xx es múltiplo de 3”. Si es múltiplo de 2 y de 3 deben aparecer los dos mensajes. 
Si no es múltiplo de ninguno de los dos el programa finaliza sin mostrar ningún mensaje.
'''

numero = int(input("Intraduzca el numero:"))

if numero % 2 == 0:
    print("El %s es multiplo de 2" % (numero))
elif numero / 3 == 0:
    print("El %s es multiplo de 3" % (numero))
    
else:
    print()

'''
4. Realizar un programa que lea la edad de una persona menor a 100 años e informe de si es un niño (0-12 años), un adolescente 
(13-17), un joven (18- 29) o un adulto.
'''

Edad = int(input("Dime tu edad :"))

if 0 <= Edad <= 12:
    print("Eres un niño")

elif 13 <= Edad <= 17:
    print("Eres un adolescente")

elif 18 <= Edad <= 29:
    print("Eres un joven")

else:
    print("Eres un adulto")

'''
5. Realizar un programa que solicite 4 números e imprima la media de los números. También debe imprimir aquellos números que 
son superiores a la media.
'''

Numero1 = int(input("Dime un numero:"))
Numero2 = int(input("Dime un numero:"))
Numero3 = int(input("Dime un numero:"))
Numero4 = int(input("Dime un numero:"))

Media = (Numero1 + Numero2 + Numero3 + Numero4) / 4

if Media < Numero1:
    print("El numero %s es mayor a la media de los numeros que es %s" % (Numero1, Media))
    
if Media < Numero2:
    print("El numero %s es mayor a la media de los numeros que es %s " % (Numero2, Media))
    
if Media < Numero3:
    print("El numero %s es mayor a la media de los numeros que es %s" % (Numero3, Media))
    
if Media < Numero4:
    print("El numero %s es mayor a la media de los numeros que es %s" % (Numero4, Media))


'''
6. Realizar un programa que solicite un carácter por teclado e informe por pantalla si el carácter es una vocal o no lo es. 
Si es una vocal mostrará el mensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc.
'''

Caracter = input("Escribe un caracter:") 
 
if Caracter == "A":
    print("Es la primera vocal")

if Caracter == "E":
    print("Es la segunda vocal")

if Caracter == "I":
    print("Es la tercera vocal") 

if Caracter == "O":
    print("Es la cuarta vocal")

if Caracter == "U":
    print("Es la quinta vocal")

else:
    print("No es una vocal")

'''
7. Realizar un programa que lea el estado civil de una persona (S-Soltero, C- Casado, V-Viudo y D-Divorciado) y su edad. 
Después debe mostrar por pantalla el porcentaje de retención que debe aplicársele de acuerdo con las siguientes reglas:
 A los solteros o divorciados menores de 35 años, un 12%
 Todas las personas mayores de 50 años, un 8.5%
 A los viudos o casados menores de 35 años, un 11.3%
 Al resto de casos se le aplica un 10.5%
'''

EstadoCivil = input("Dime tu estado civil:")

Edad = int(input("Dime tu edad:"))

if (EstadoCivil == "S" or EstadoCivil == "D") and  Edad < 35:
    print("Su porcentaje de retencion es del 12%")

if Edad > 50:
    print("Su porcentaje de retencion es del 8,5%")
    
if (EstadoCivil == "V" or EstadoCivil == "C") and Edad < 35:
    print("Su porcentaje de retencion es del 11,3%")
    
else:
    print("Su porcentaje de retencion es del 10,5% ")
    

'''
8. Realizar un programa que lea por teclado dos marcaciones de un reloj digital (horas, minutos, segundos) comprendidas entre 
las 0:0:0 y las 23:59:59 e informe cual de ellas es mayor.
Ejemplo:
Hora 1: 12:35:37
Hora 2: 12:38:36
“Hora 2 es mayor”
'''

Hora1 = int(input("Dime una hora:"))
minuto1 = int(input("Dime una hora:"))
segundo1 = int(input("Dime una hora:"))
Hora2 = int(input("Dime una hora:"))
minuto2 = int(input("Dime una hora:"))
segundo2 = int(input("Dime una hora"))

if 0 <= Hora1 <= 24 and 0 <= Hora2 <= 24 and 0 <= minuto1 <= 59 and 0 <= minuto2 <= 59 and 0<= segundo1 <= 59:

    if Hora1 > Hora2:
        print("La hora 1 es mayor que la hora 2")

    elif Hora1 < Hora2:
        print("La hora 2 es mayor que la hora 1")

    else:
        print("La hora son iguales")

        if minuto1 > minuto2:
            print("La hora 1 es mayor que la hora 2")
    
        elif minuto1 < minuto2:
            print("La hora 1 es menor que la hora 2")
    
        else:
            print("La hora son iguales")
    
            if segundo1 > segundo2:
                print("La hora 1 es mayor que la hora 2")

            elif segundo1 < segundo2:
                print("La hora 1 es menor que la hora 2")

            else:
                print("La hora son iguales")


'''
9. En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El porcentaje de rebaja que se aplicará sobre el 
precio original del producto se calcula de la siguiente forma:
 Si el producto es de tipo A, independientemente de su precio se aplica un 7% de descuento.
 Si el producto es de tipo C o bien el precio es inferior a 500€ se aplicará un porcentaje del 12% de descuento.
 En el resto de casos se aplica un 9% de descuento.

Realizar un programa que solicite los datos necesarios (tipo de producto y precio original) y calcule el precio rebajado. 
Debe comprobarse que los datos de entrada son correctos, y si no lo son mostrar un mensaje de error.
'''

Tipodeproducto = input("Dime el tipo de producto:")
PrecioOriginal = int(input("Dime el precio original:"))

if Tipodeproducto == "A" or Tipodeproducto == "B" or Tipodeproducto == "C":

    if Tipodeproducto == "A":
        print("El precio final es de %s" % (PrecioOriginal * 0.93))

    if Tipodeproducto == "C" or PrecioOriginal < 500:
        print("El precio final es de %s" % (PrecioOriginal * 0.88))
    
    else:
        print("El precio final es de %s" % (PrecioOriginal * 0.91))



'''
10. Realizar un programa que lea un carácter y dos números enteros por teclado. Si el carácter leído es un operador aritmético, 
calcular la operación correspondiente, si es cualquier otro debe mostrar un error.
'''

Caracter = input("Dime un caracter:")
Numero1 = int(input("Dime un numero:"))
Numero2 = int(input("Dime un numero:"))

if Caracter == "+":
    print("Tu caracter es %s " % (Caracter))
    print("El resultado es: %s" % (Numero1 + Numero2))
elif Caracter == "-":
    print("Tu caracter es %s " % (Caracter))
    print("El resultado es: %s" % (Numero1 - Numero2))
elif Caracter == "*":
    print("Tu caracter es %s " % (Caracter))
    print("El resultado es: %s" % (Numero1 * Numero2))
elif Caracter == "/":
    print("Tu caracter es %s " % (Caracter))
    print("El resultado es: %s" % (Numero1 / Numero2))

    