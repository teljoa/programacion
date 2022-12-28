'''
 En el gimnasio Jacafitness tienen el siguiente horario: Los Lunes, Miércoles y Viernes imparten Spinning de 12 a 14, Yoga de 16 a 20 y Body combat de 20 a 22; 
 Los Martes y Jueves La sesión de Spinning y Yoga se intercambian.

Elabora un programa que dé la bienvenida al gimnasio Jacafitness y tras preguntar por la hora y el día de la semana te indique la actividad que puedes realizar.
'''

print("Bienbenido al gimnasio Jacafitness")

Dia = input("Dime un dia de la semana:")
Hora = int(input("dime una hora del dia:"))
    
if Dia == "Lunes" or Dia == "Miercoles" or Dia == "Viernes":
    
    if 12 <= Hora <= 14:
        print("Durante estas horas del dia de hoy se realiza Spinning")  
    
    if 16 <= Hora <= 20:
        print("Durante estas horas del dia de hoy se realiza Yoga")  
    
    if 20 <= Hora <= 22:
        print("Durante estas horas del dia de hoy se realiza Body combat")
        
if  Dia == "Martes" or Dia == "Jueves":
    
    if 12 <= Hora <= 14:
        print("Durante estas horas del dia de hoy se realiza Yoga") 
    
    if 16 <= Hora <= 20:
        print("Durante estas horas del dia de hoy se realiza Spinning")
          
    if 20 <= Hora <= 22:
        print("Durante estas horas del dia de hoy se realiza Body combat")

if Dia == "Sabado" or Dia == "Domingo":
    print("El dia de hoy el gimnasio esta cerrado") 
    
if 0 <= Hora <= 11 or 14 < Hora < 16 or 22 < Hora < 24:
    print("A estas horas del dia no hay ninguna actividad")












