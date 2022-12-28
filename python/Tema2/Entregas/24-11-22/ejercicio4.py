'''
4. Crea un programa que lea por teclado números de forma sucesiva y los guarde en
una lista; el proceso de lectura y guardado finalizará cuando metamos un número
negativo. En ese momento se mostrará el elemento mayor y los números pares.
'''
n = []
tmp =0

while tmp >=0:
    tmp = int(input("Dime un numero:"))
    if tmp%2 ==0:
        n.append(tmp)

print(n)

    