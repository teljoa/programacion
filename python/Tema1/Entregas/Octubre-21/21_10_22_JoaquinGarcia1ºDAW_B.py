'''
En el gimnasio Jacatfitness para el que ya hemos trabajado nos piden que realicemos un programa para determinar si deberías acudir 
al médico para que te haga una revisión, para ello debemos hacer las siguientes preguntas:

        ¿Peso?

        ¿Edad?

        ¿Tipo de vida? (Sedentaria/Activa/Muy activa)

El programa terminará si se introduce un peso negativo. Se deben comprobar que los datos son correctos y si no lo son, se deben 
volver a preguntar. Las recomendaciones para ir al médico son:

    Si tienes más de 70 años y lleva una vida Sedentaria

    Si pesa más de 100 kg sea cual sea la edad.

    Si pesa más de 74,4 kg y tiene más de 50 años

En cualquier otro caso se mostrará “No es urgente que acuda al médico si no tiene problemas de salud”
'''

peso = float(input("Dime cual es tu peso(kg):"))
edad = int(input("Dime cual es tu edad:"))
tipoVida = (input("Dime cual es tu estilo de vida (Sedentaria/Activa/Muy activa):"))

while (0 < peso <= 500) or (0 < edad <= 105) or (tipoVida == "Sedentaria" or tipoVida == "Activa" or tipoVida == "Muy activa"):
    print("Los datos intraducidos no son correctos, vuelve a introducirlos.")
    peso = float(input("Dime cual es tu peso(kg):"))
    edad = int(input("Dime cual es tu edad:"))
    tipoVida = (input("Dime cual es tu estilo de vida (Sedentaria/Activa/Muy activa):"))

    
if edad > 70 and tipoVida == "Sedentaria":
    print("Uste deberia de ir al medico")
elif peso > 100:
    print("Uste deberia de ir al medico")    
elif peso > 74.5 and edad > 50:
    print("Uste deberia de ir al medico")
else:
    print("No es urgente que acuda al médico si no tiene problemas de salud")
    
    
    
    