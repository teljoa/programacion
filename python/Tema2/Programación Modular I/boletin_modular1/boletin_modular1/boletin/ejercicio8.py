'''
8. Realiza un programa que añada números enteros a una lista hasta que se
introduzca un número negativo. Haciendo uso de esta lista, elabora funciones que
devuelvan:
a. una lista con todos los que sean primos.
b. el sumatorio
c. el promedio de los valores.
d. una lista con el factorial de cada uno de esos números.
'''
numeros = []
tmp = int(input(' Numero:'))
while tmp>= 0:
    numeros.append(tmp)  
    tmp = int(input(' Numero:'))

  


def esPrimo(num):    
    valido = True
    k=2
    while (k<num and esPrimo):
        if num%k==0:
            valido = False
        k += 1
    return valido       
     
def primosLista(aList): 
    tmp = []
    for n in aList:
        if esPrimo(n):
            tmp.append(n)
    return tmp
    
def sumatorio(aList):
    tmp = 0 
    for n in aList:
        tmp += n
    return tmp

def media (aList):
    tmp = sumatorio(aList)
    
    return tmp / len(aList)

def factorial(num):
    tmp = 1
    for n in range(1,num+1):
        tmp *= n
    return tmp

def factorialLista(aList):
    tmp = []
    for n in aList:
        tmp.append(factorial(n))
    return tmp

print(numeros)
print(primosLista(numeros))  
print(sumatorio(numeros))
print(media(numeros))
print(factorialLista(numeros))