'''
12. Escribe una función unionListas que reciba dos listas y devuelva los elementos que
pertenecen a una, o bien, a la otra, pero sin repetir ninguno (unión de conjuntos)
'''
a = ['a','b','c',2,4,6,'D']

b = ['1', 'b',7,2,1,6,9,'D']

def unionListas(aList, bList):
    tmp = []
    for n in aList:
        if n not in bList:
            tmp.append(n)
    for i in bList:
        if i not in aList:
            tmp.append(i)
    
    return tmp

print(unionListas(a, b))