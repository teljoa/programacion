'''
2. Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente.
'''
numeros = [2,13,4,15,164,1,17,19,0]

def imprimirComas (aL =[]):
    return(', '.join(map(str,aL))) 

def desplazar (aL = [],cantidad = 1, orden = 'd'):
    cantidad = cantidad % len(aL) 
    orden =  orden.upper().strip()
    tmp = []
    if orden == 'D':
        for n in range(len(aL)):            
            tmp.append(aL[n-cantidad])
        return tmp
    elif orden == 'I':    
        for n in range(len(aL)):
            tmp.append(aL[-len(aL)+n+cantidad]) #Es un poco lioso, pero es la mejor forma para evitar salirme del rango
    return tmp