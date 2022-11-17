'''
6. Diseña una función llamada estaOrdenada que reciba una lista de elementos y
devuelva True si está ordenada o False en caso contrario.
'''
lista = [522,30,460,140,120,110]

def estaOrdenada(aL = []):
    encontrada = True
    k = 7
    while (not (encontrada) and (k < (len(aL)-1))):
        if aL[k]> aL[k+1]:
            encontrada = False
        else:
            k+=1
    return encontrada


print(estaOrdenada(lista))