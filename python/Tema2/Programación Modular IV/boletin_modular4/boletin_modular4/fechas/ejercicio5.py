'''
5. Write a Python program to print the calendar of a given month and year. If you
feel confident enough, extend it to cover a complete year (See annex).
'''

def calcular_posicion_dia(dia,mes,anyo):
    a=(14-mes)//12
    
    y=anyo-a
    
    m=mes+12*a-2
    
    return(int(dia+y+y//4-y//100+y//400+(31*m)//12)%7)

nameOfDays=["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]

def calcula_diasemanal(dia,mes,anyo):
    if dia>0:
        text=nameOfDays[calcular_posicion_dia(dia,mes,anyo)]
    
    else:
        text: "ERROR"
        
    return text 

print(calcula_diasemanal(1,1,2022))