list = [0,1,4,2,7,5,8,6,3]

def get_posicion_eq_valor(list):
    s = []
    for i in range(len(list)):
        if i == list [i]:
            s.append(i)
    
    return s

print(get_posicion_eq_valor(list))

lista=[8,8,8,8,8,8,8,8,8]
            
def obtener_frecuencia(lista):
    a=0
    for i in range(len(lista)):
        if i == i:
            a+=1
    return print((i),"frecuencia:",(a))

print(obtener_frecuencia(lista))

def dame_numero():
    from random import randint
    return randint(0,20)

def lista_aleatoria():
    list1=[]
    list2=[]
    for i in range(10):
        list1.append(dame_numero())
    for i in range(30):
        list2.append(dame_numero())
    
    return [list1,list2]

print(lista_aleatoria())