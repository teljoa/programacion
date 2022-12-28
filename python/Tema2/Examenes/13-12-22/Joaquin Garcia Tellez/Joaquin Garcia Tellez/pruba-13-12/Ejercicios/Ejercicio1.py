def generar_digito_contol(numeross):
    numeross = int(numeross)
    cc = int(numeross)%97
    return cc

def es_emitido_andalucia(numeross):
    if numeross[0:2] == [0,4]:
        validador = True
    elif numeross[0:2] == [1,1]:
        validador = True 
    elif numeross[0:2] == [1,4]:
        validador = True 
    elif numeross[0:2] == [1,8]:
        validador = True 
    elif numeross[0:2] == [2,1]:
        validador = True 
    elif numeross[0:2] == [2,3]:
        validador = True 
    elif numeross[0:2] == [2,9]:
        validador = True 
    elif numeross[0:2] == [4,1]:
        validador = True  
    else:
        validador=False
        
    return validador 

print(es_emitido_andalucia([0,2,5,4,6,7,1,5,7,2,6,3]))
print(es_emitido_andalucia([0,4,5,4,6,7,1,5,7,2,6,3]))
    