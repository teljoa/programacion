'''
6. Design a method called getNumberOfDigits that receives one number (it can be
real, integer, positive or negative) and should return the number of digits it contains. If
the parameter is not valid the method should return None. Extend this function to
other numeric systems (hexadecimal, decimal, binary, octal).
'''
def esbinario(tmp):
    valido = True
    for i in range(len(str(tmp))):
        if str(tmp)[i] not in ["0","1","-1","0.","1.","-1."]:
            valido = False
    
    return valido

def esdecimal(tmp):
    valido = True
    for i in range(len(str(tmp))):
        if not(type (tmp) == int):
            valido = False
    
    return valido

def esoctal(tmp):
    valido = True
    for i in range(len(str(tmp))):
        if str(tmp)[i] not in ["0","1","2","3","4","5","6","7","-1","-2","-3","-4","-5","-6","-7","0.","1.","2.","3.","4.","5.","6.","7.","-1.","-2.","-3.","-4.","-5.","-6.","-7."]:
            valido = False
    
    return valido
        
def eshex(tmp):
    valido = True
    for i in range(len(str(tmp))):
        if str(tmp)[i] not in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","-1","-2","-3","-4","-5","-6","-7","-8","-9","-a","-b","-c","-d","-e","-f"]:
            valido = False
    
    return valido

def getNumberOfDigits(opcion,tmp):
    if opcion=="a":
        if eshex(tmp) == True:
            print("valido")
        else:
            None
    elif opcion=="b":
        if esdecimal(tmp) == True:
            print("valido")
        else:
            None
    elif opcion=="c":
        if esbinario(tmp) == True:
            print("valido")
        else:
            None
    elif opcion=="d":
        if esoctal(tmp) == True:
            print("valido")
        else:
            None
    else:
        print("Opcion no valida")


(getNumberOfDigits("a",110))
(getNumberOfDigits("b",110))
(getNumberOfDigits("c",110))
(getNumberOfDigits("d",110))
