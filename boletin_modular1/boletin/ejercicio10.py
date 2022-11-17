'''
10. Diseña una función conversor que convierta un número de binario a decimal o de
decimal a binario. Esta función recibirá un número en formato de cadena de texto
cuya última posición indica el sistema numérico utilizado (D-decimal, B-binario).
Debe validar la información, así, por ejemplo, el número ‘1020101B’ no sería válido
puesto que los valores en binario son 0 y 1
'''
def binarioValido (cad):
    valido = True
    k = 0
    cad = cad.upper()
    while k<len(cad[:-1]) and valido:
        if cad[k] not in map(str,[0,1]):
            valido = False
        k += 1
    if valido and cad[-1] != 'B':
        valido = False
         
    return valido

def invertirCadena (cad):
    tmp = ''
    for n in range(len(cad)-1,-1,-1):
        tmp = tmp + cad[n]
    return tmp

def binario2decimal(cad):
    tmp = 1
    cad = cad[:-1]    
    cad = invertirCadena(cad)
      
    for n in range(len(cad)):
        if cad[n] == '1':
            tmp += 2**n
            
    return (tmp -1)

def decimalValido (cad):
    valido = True
    k = 0
    cad = cad.upper()
    while k<len(cad[:-1]) and valido:
        if cad[k] not in map(str,[0,1,2,3,4,5,6,7,8,9]):
            valido = False
        k += 1
    if valido and cad[-1] != 'D':
        valido = False
         
    return valido

def maximoBinario(num):
    maximoValor = 0
    while (2**(maximoValor+1)) <= num:
        maximoValor += 1
    return maximoValor
    
def decimal2binario (cad):
    num = int(cad[:-1])
    tmp = ''
    maxi =  maximoBinario(num)   
    for n in range(maxi,-1,-1):
        if (num - 2**n) >= 0:
            tmp += '1'
            num = (num - 2**n) 
        else:
            tmp += '0'
    return tmp

print(' Conversor binario-decimal y decimal-binario')
cadena = input(' Introduzca el numero (formato 120D o 010101B):')

if binarioValido(cadena):
    print(binario2decimal(cadena))
elif decimalValido(cadena):
    print(decimal2binario(cadena))