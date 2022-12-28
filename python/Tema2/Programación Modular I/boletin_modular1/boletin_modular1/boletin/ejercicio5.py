'''
5. Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’,
‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].
'''
lista = [1,2,3,4,5]

def reverse(aList):
    tmp = []
    for n in range(len(aList)):
        tmp.append(aList[(-n-1)])
    return tmp

print(lista)
print(reverse(lista))