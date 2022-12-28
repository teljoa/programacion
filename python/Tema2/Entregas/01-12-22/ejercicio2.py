'''
Ejercicio2
'''

def validador_letra(dni):
    letras="TRWAGMYFPDXBNJZSQVHLCKE"
    numeros=dni[:-1]
    numeros= numeros%23
    resultado = False
    
    if dni[-1].upper() == letras[numeros]:
        resultado = True
    
    return resultado

def validador_dni(dni):
    valido = True
    
    if len(dni) == 9:
        for i in range(len(dni)):
            if dni[i] not in "1234567890":
                if dni[i] not in "TRWAGMYFPDXBNJZSQVHLCKE":
                    if i == (len(dni)-1):
                        pass
                    else:
                        valido = False
        
    return valido



def dni_validador(dni):
    valido = True
    
    if not(validador_letra(dni) and (validador_dni(dni))):
        valido = False
    
    return valido

print(dni_validador("34692475J"))
