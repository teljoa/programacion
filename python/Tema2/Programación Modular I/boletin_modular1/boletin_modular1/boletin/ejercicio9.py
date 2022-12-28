'''
9. Desarrolla un programa que a partir de una lista de números y un entero k, realice la
llamada a tres funciones: a) para devolver una lista de números con los menores de
k, b) otra con los mayores y c) otra con aquellos que son múltiplos de k.
'''
lista = [1,2,3,4,5,6,7,8,9,0,10,48,13,5216]

k = 7


def menoresQue(aList, num):
    tmp = []
        
    for n in aList:
        if n < num:
            tmp.append(n)
            
    return tmp

def mayoresQue(aList, num):
    tmp = []
        
    for n in aList:
        if n > num:
            tmp.append(n)
            
    return tmp

def multiplosDe(aList, num):
    tmp = []
        
    for n in aList:
        if ((n%num == 0) and (n != 0)):
            tmp.append(n)
            
    return tmp

print(f' Los numeros menores que {k} son {menoresQue(lista,k)}')
print(f' Los numeros mayores que {k} son {mayoresQue(lista,k)}')
print(f' Los numeros multiplos de {k} son {multiplosDe(lista,k)}')