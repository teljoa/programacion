'''
1. Función que dado un instante (horas, minutos y segundos) devuelva el número
de segundos transcurridos desde el inicio de un día hasta ese instante.
'''
def calcula_tiempo(h,m,s):
    tr=86400-((h*60)+(m*3600)+(s*216000))
    return tr

print(calcula_tiempo(14,25,56))