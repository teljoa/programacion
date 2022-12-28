'''
4. Crea un programa que lea por teclado números de forma sucesiva y los guarde en
una lista; el proceso de lectura y guardado finalizará cuando metamos un número
negativo. En ese momento se mostrará el elemento mayor y los números pares.
'''
numeros = []
tmp = int(input(' Numero:'))
while tmp>= 0:
    numeros.append(tmp)  
    tmp = int(input(' Numero:'))
    
print(numeros)