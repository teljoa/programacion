def es_primo(numero):
    esPrimo = True
    
    if numero > 2:
        for i in range(2, numero):
            if numero%i==0:
                esPrimo = False
                
    return esPrimo


for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
    print(i, es_primo(i))