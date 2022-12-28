'''
10. Escribir una función que, devuelva el número de palabras que hay en una cadena que recibe
como parámetro. Ten en cuenta que entre dos palabras puede haber más de un blanco.
También al principio y al final de la frase puede haber blancos redundantes.
Por ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3
'''
def numeroPalabra(cad):
    c = 0
    solucion = 0
    cad = cad.strip()
    while c < len(cad):
        while c < len(cad) and cad[c] ==" ":
            c += 1
        solucion += 1
        while  c < len(cad) and cad[c] !=" ":
            c += 1
    return solucion

print (numeroPalabra("He estudiado mucho"))