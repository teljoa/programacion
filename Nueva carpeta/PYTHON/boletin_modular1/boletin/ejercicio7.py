'''
7. Escribir una función denominada encajan que indique si dos fichas de dominó
encajan o no. Las fichas son recibidas en dos cadenas de texto con el siguiente
formato.

[3,4] [2,5]
'''
a,b = [3,4],[2,5]

def encajan(a,b):
    if a[0] in b or a[1] in b:
        return True
    return False

print(encajan(a, b))