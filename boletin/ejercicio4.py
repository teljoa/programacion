'''
4. Design a method called getDayOfWeek that receives a list containing three integers
(day, month and year) and returns the day of the week for that date (Monday,
Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday).

You can use the following algorithm to get a number between 0 (Sunday) and 6
(Saturday) corresponding to the day in the week for a given date:
a = (14 - month) / 12
y = year – a
m = month + 12 * a – 2
d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7
'''

def getday0fWeek(dia,mes,año):
    a=(14-mes)//12
    
    y=año-a
    
    m=mes+12*a-2
    
    return(int(dia+y+y//4-y//100+y//400+(31*m)//12)%7)

nameOfDays=["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
dia=1
while dia>0:
    dia=int(input("Introduce un muenro de dia:"))
    mes=int(input("Introduce un numero de mes:"))
    año=int(input("Introduce un numero de año:"))
    if dia>0:
        text=nameOfDays[getday0fWeek(dia,mes,año)]
    
    else:
        text: "ERROR"
        
    print("Es",text)
    
