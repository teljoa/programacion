'''
9. Crear una función que, tomando una cadena de texto como entrada, construya y devuelva
otra cadena formada de la siguiente manera: el método debe colocar todas las consonantes
al principio y todas las vocales al final de la misma, eliminando los blancos.
Por ejemplo, pasándole la cadena "curso de programacion", una posible solución sería
"crsdprgrmcnuoeoaaio
'''

def descadena(cad):
    cad = cad.lower()
    solucion = ''
    for n in cad:
        if n in "qwrtypsdfghjklñzxcvbnm":
            solucion += n
            
    for n in cad:
        if n in "aeiou":
            solucion += n
    return solucion

            
assert(descadena('curso de programacion') == "crsdprgrmcnuoeoaaio")
print(descadena('curso de programacion'))