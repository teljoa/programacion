''' boletin 4 ejercicios de bucle'''

'''
17. Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario
'''

Numero1 = int(input("Dime un numero:"))
Numero2 = int(input("Dime un numero:"))

for par in range(Numero1, Numero2, 2):
    print(par)

'''
18. Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite
inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine
el programa dará las siguientes informaciones:
◦ La suma de los números que están dentro del intervalo (intervalo abierto).
◦ Cuantos números están fuera del intervalo.
◦ Informa si hemos introducido algún número igual a los límites del intervalo.
'''

Inferior = int(input("Dime un numero:"))
Superior = int(input("Dime un numero:"))

tmp = -1
Contadorfuera = 0
contadorigual = 0
SumadorDentro = 0

while Inferior > Superior:
    Inferior = int(input("El limite inferior es superior al limite superior, vuelve a meter el limite inferior:"))

while tmp!= 0:
    tmp = int(input("Indique un numero:"))
    
    if tmp == Inferior or tmp == Superior:
        contadorigual = contadorigual +1
    elif Inferior < tmp < Superior:
        SumadorDentro = SumadorDentro + tmp
    else:
        Contadorfuera = Contadorfuera + 1

print("Han sido %s numeros iguales a alguno de los dos limites, %s fuera del intervalo y la suma de los 2 intervalos es de %s" % (tmp, tmp, Inferior + Superior))

'''
19. Escribe un programa que dados dos números, uno real (base) y un entero positivo
(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.
'''

Base = int(input("Dime un numero:"))
Potencia = int(input("Dime un numero:"))

print(Base**Potencia)

'''
20. Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el
segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar
cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses.
'''

p =  10
t = 0
for i in (1/20):
    p = p*2
    t =  t + p
    print("EN EL MES", i, "PAGARAS: $", p)

print("EL TOTAL QUE PAGASTE EN 20 MESES ES DE: %$" %(t))

'''
21. Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.
'''

start = 11
end = 25
  
for i in range(start, end+1): 
    if i>1: 
        for j in range(2,i): 
            if(i % j==0): 
                break
    else: 
        print(i) 
        
        
'''Boletin6'''        

'''
1. Design a program to show all numbers between 1 and 100. If the number is a multiple of 7 you should show the message "The number xx is a multiple of 7". If 
the number is a multiple of 13 you should show the message "The number xx is a multiple of 13". If the number is a multiple of 7 and 13 you should show both
messages.
'''

import numbers

for multiple in range(1,101):
    print(multiple)
    if multiple % 7 == 0:
        print("El s% es multiplo de 7" %(multiple))
    elif multiple % 13 == 0:
        print("El s% es multiplo de 13" %(multiple))
    elif (multiple % 7 == 0) and (multiple % 13 == 0):
        print("El s% es multiplo de 7 y de 13" %(multiple))

'''
2. Design a program for reading an integer between 0 and 10 and show the times table. To ask for the number you should show the next message "Enter one number
between 0 and 10”. If the number is out of the boundaries, the program should show the message “The number is out of the boundaries”. If the number is valid, it 
should show the times table following the next format:
7*0=0
7*1=7
.....
7*10=70
'''

numbers = int(input("Dime un numero entre el (0 - 10):"))

if 0 <= numbers <= 10:
    for integer in range(1,11):
        print(numbers * integer)
else:
    print("El numero esta fuera del limite, vuelve a introducirlo")

'''
3. Design a program that asks how many numbers the user wants to introduce. Then, the user would have to introduce the numbers one by one and the program should
say if each one of the numbers is odd or even. If the user inputs 0 or a negative number, it is not valid, and the system should ask for another number. 
The messages are the following:

“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not valid.
“The number XX is odd”
“The number XX is even”
'''

numero = int(input("Enter one number:"))
peque = numero

pregunta = input("Do you wnt to enter more number (Y/N)")

while pregunta.upper()=="Y":
    numero = int(input("Enter one number:"))
    if numero < peque:
        peque = numero
    pregunta = input("do you want to enter more number (Y/N)")
    
print(f"The smallest number is {peque}")

'''
4. Design a program that reads a positive number N greater than 0 and show the result of the sum of the N numbers between 1 and N. If the number N is not valid, 
the program should ask for it again. The messages are the following:

“Enter one number greater than 0:”
“The number is not right, try again.”
“The sum of the N first numbers is XX.”
'''

numero = int(input("Enter one number greater than 0:"))

while numero < 0:
    print("The number is not right, try again.")
    
for sum in range(1, numero):
    print(f"The sum of the N first numbers is {numero + (numero - 1)}")

'''
5. Design a program that asks for numbers until the user inputs a negative one. When this happens, the program will show how many positive numbers have been 
introduced by the user. The messages are the following:

“Enter a number (negative to finish):”
“You have entered XX positive numbers.”
'''

numero = int(input("until the user inputs:"))
total = 0

for i in range(numero):
    numero = int(input("Enter one number greate than 0:"))
    while numero <= 0:
        numero = int(input("Enter a number (negative to finish)."))
    
    total += numero
    if i <= 0:
        print(f"You have entered XX positive numbers{total+numero}")    

'''
6. Design a program that reads two integer numbers, for example numberA and numberB, and calculates the product of both numbers without use multiplication, but
using the sum. The messages are the following:

“Enter one number:”
“The product is XX”
'''

numeroA = int(input("Enter one number:"))
numeroB = int(input("Enter one number:"))
suma = 0

for i in range(numeroA, numeroB):
    suma +=numeroB

print("The product is %" %(suma))


'''
7. Design a program that asks how many numbers the user wants to write. After the user enters all numbers, the program should say the medium of the numbers. 
If the user inputs a wrong number, the program should ask for it again. The messages are the following:

“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not valid.
“The medium is XX.XX” to show the result.
'''

cantidad = int(input("How many numbers do you want input?"))

while cantidad <= 0:
    cantidad = int(input("How many numbers do you want input?"))
    
total = 0

for i in range(cantidad):
    numero = int(input("Enter one number greate than 0:"))
    while numero <= 0:
        numero = int(input("The number is not valid, it should be greater than 0 to inform that the number is not valit."))
    
    total += numero
    
print(f"The medium is{total/cantidad}")

'''
8. Design a program that asks for a set of numbers. After inputting each number, the program should ask “Do you want to enter more numbers (Y/N)?”. If the answer 
is “Y” the program asks for other numbers. When the user finishes to enter all the numbers, the program should say which one is the smallest. The messages are the 
following:

“Enter one number:”
“Do you want to enter more number (Y/N)?”
“The smallest number is XX”
'''

numero = int(input("Enter one number:"))
peque = numero

pregunta = input("Do you wnt to enter more number (Y/N)")

while pregunta.upper()=="Y":
    numero = int(input("Enter one number:"))
    if numero < peque:
        suma = numero
    pregunta = input("do you want to enter more number (Y/N)")
    
print(f"The smallest number is {suma}")

'''
9. Design a program that reads an integer positive number greater than 0 and says if it’s a “perfect number”. A number is perfect if it is equal to the sum of all 
its divisors. The messages are the following:

“Enter an integer positive number greater than 0:”
“The number is not valid, try again.”
“The number is perfect.”
“The number is not perfect.”
'''

numero = int(input("Enter an integer positive number greater than 0:"))
perfect = 0

while numero < 0:
    print("The number is not valid, try again.")
    int(input("Enter an integer positive number greater than 0:"))

perfect += numero

for i in range (numero % perfect ==0):
    if (numero // i)+i== numero:
        print("The number is perfect.") 
    else:
        print("The number is not perfect.")


'''
10. Design a program that reads an integer positive number and says the “factorial” of the number. To calculate the factorial you should know that:

FACT(0)= 1
FACT(1) =1
FACT(N)= N*(N-1)*(N-2)*....1
The messages are the following:
“Enter an integer positive number:”
“The number is not valid, try again.”
“The factorial is XX”
'''

numero = int(input("Dime un numero:"))
total = 1

while numero > 0:
    total = total * numero
    numero -=1
    
print(total)
