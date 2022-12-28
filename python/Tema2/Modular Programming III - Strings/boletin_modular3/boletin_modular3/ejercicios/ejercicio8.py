'''
8. Diseñar una función que determine la cantidad de vocales diferentes, que tiene una palabra
o frase introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2.
'''
def DistintasVocales(cad):
    tmp = []
    cad = cad.lower()
    for n in cad:
        if n in "aeiou":
            if n not in tmp:
                tmp.append(n)
    return len(tmp)


print(DistintasVocales("abaco"))