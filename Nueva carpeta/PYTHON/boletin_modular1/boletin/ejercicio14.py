'''
14. Escribe una función que, dada una lista de cadenas, devuelva la cadena más larga.
Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá la
que tenga el mayor número de caracteres repetidos .
'''

lista = ['isodjgiksgjñljksegñk']
lista = ['krljheeeeeeeeeeeeesósdkñljgl']

def contarLetra(cadena,letra):
    k = 0
    letra = letra.lower()
    cadena = cadena.lower()
    for n in cadena:
        if letra == n:
            k += 1
    return [letra, k]

def esta(letra, lista):
    
    for n in lista:
        if letra in n:
            return True
    return False

def contarRepetidos(cadena):
    cadena = cadena.lower()
    tmp = []
    tmp.append(contarLetra(cadena, cadena[0]))
    for n in cadena.lower():
        if not (esta(n,tmp)):
            tmp.append(contarLetra(cadena, n))
    return tmp


    
maximo = lista[0]
for n in lista:
    if len(n) > len(maximo):
        maximo = n
    elif len(n) == len(maximo): 
        if len(contarRepetidos(n)) < len(contarRepetidos(maximo)):#mientras menor sea el tamaño mas letras repetidas tiene
            maximo = n
        
        
print(maximo)