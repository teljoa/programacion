'''
1. Escribe el código de un programa que reciba un número de nota de 0 a 100 y nos informe de las calificaciones en el siguiente 
formato:

90-100, Sobresaliente
70-89, Notable
60-69, Bien
50-59, Suficiente
0-49, Suspenso
'''
'''
nota = float(input("Dime tu nota:"))

if 90 <= nota <= 100:
    print("Tu nota corresponde a un Sobresaliente")
elif 70 <= nota <= 89:
    print("Tu nota corresponde a un Notable")
elif 60 <= nota <= 69:
    print("Tu nota corresponde a un Bien")
elif 50 <= nota <= 59:
    print("Tu nota corresponde a un Suficiente")
elif 0 <= nota <= 49:
    print("Tu nota corresponde a un Suspenso")
'''
'''
2. Escribe una aplicación que pida la fecha actual (día y mes) y el hemisferio (Norte/Sur) e indique en qué estación se encuentra:

a. Hemisferio Norte: Otoño (desde 23 Septiembre), Invierno (desde 21 diciembre), Primavera (desde 21 Marzo), Verano 
(desde 21 Junio).

b. Hemisferio Sur: Primavera (desde 23 Septiembre), Verano (desde 21 diciembre), Otoño (desde 21 Marzo), Invierno 
(desde 21 Junio).
'''
'''
dia = int(input("Dime que dia es hoy:"))
mes = input("Dime que mes es:")
hemisferio = input("Dime en que hemisferio te encuentras:")

if (0 < dia <= 31) and (mes== "Enero" or mes == "Febrero" or mes == "Marzo" or mes == "Abril" or mes == "Mayo" or mes == "Junio" or mes == "Julio" or mes == "Agosto" or mes == "Septiembre" or mes == "Octubre" or mes == "Nobiembre" or mes == "Diciembre") and (hemisferio == "S" or hemisferio == "N"):
    if (23 <= dia <= 30 and mes == "Septiembre") or (0 < dia <=31 and mes == "Octubre") or (0 < dia <= 21 and mes == "Nobiembre") or (0 < dia <=20 and mes == "Diciembre"):
        if hemisferio == "N":
            print("Otoño")
        elif hemisferio == "S":
            print("Primavera")

    elif (21 <= dia <= 31 and mes == "Diciembre") or (0 < dia <= 31 and mes== "Enero") or (0 < dia <= 28 and mes == "Febrero") or (0 < dia < 20 and mes == "Marzo" ):
        if hemisferio == "N":
            print("Invierno")
        elif hemisferio == "S":
            print("Verano")

    elif (21 <= dia <= 31 and mes == "Marzo") or (0 < dia <= 30 and mes == "Abril") or (0 < dia <= 31 and mes == "Mayo") or (0 < dia <= 20 and mes == "Junio"):
        if hemisferio == "N":
            print("Primavera")
        elif hemisferio == "S":
            print("Otoño")
    elif (21 <= dia <= 30 and mes == "Junio") or (0 < dia <= 31 and mes == "Julio") or (0 < dia <= 31 and mes == "Agosto") or (0 < dia <= 22 and mes == "Septiembre"):
        if hemisferio == "N":
            print("Invierno")
        elif hemisferio == "S":
            print("Verano")

'''
'''
3. Crea un programa que dada una fecha en formato (dd-mm-yyyy), nos devuelva cuántos días han transcurrido desde el 1 de enero de 
ese mismo año (considera que puede tratarse de un año bisiesto).
'''

day2 = int(input("Dime un dia:"))
month2 = int(input("Dime un mes:"))
year2 = int(input("Dime un año:"))

day1 = 1
month1 = 1
year1 = year2 


def diasHastaFecha(day1, month1, year1, day2, month2, year2):
    
    # Función para calcular si un año es bisiesto o no
    
    def esBisiesto(year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    
    # Caso de años diferentes
    
    if (year1<year2):
        
        # Días restante primer año
        
        if esBisiesto(year1) == False:
            diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     
        restoMes = diasMes[month1] - day1
    
        restoYear = 0
        i = month1 + 1
    
        while i <= 12:
            restoYear = restoYear + diasMes[i]
            i = i + 1
    
        primerYear = restoMes + restoYear
    
        # Suma de días de los años que hay en medio
    
        sumYear = year1 + 1
        totalDias = 0
    
        while (sumYear<year2):
            if esBisiesto(sumYear) == False:
                totalDias = totalDias + 365
                sumYear = sumYear + 1
            else:
                totalDias = totalDias + 366
                sumYear = sumYear + 1
    
        # Dias año actual
    
        if esBisiesto(year2) == False:
            diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
        llevaYear = 0
        lastYear = 0
        i = 1
    
        while i < month2:
            llevaYear = llevaYear + diasMes[i]
            i = i + 1
    
        lastYear = day2 + llevaYear
    
        return totalDias + primerYear + lastYear
    
    # Si estamos en el mismo año
    
    else:
        
        if esBisiesto(year1) == False:
            diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
        llevaYear = 0
        total = 0
        i = month1
        
        if i < month2:
            while i < month2:
                llevaYear = llevaYear + diasMes[i]
                i = i + 1
            total = day2 + llevaYear - 1
            return total 
        else:
            total = day2 - day1
            return total 
'''
4. Existen cuatro grupos sanguíneos en seres humanos, que se multiplican por dos si consideramos el factor Rh. Unos grupos son 
compatibles con otros atendiendo al criterio que podemos ver en las siguientes tablas.



Elabora un programa que reciba dos grupos sanguíneos y devuelva si son compatibles y en qué sentido.
Por ejemplo, si se recibe A y B debería decir que no son compatibles.
Por el contrario, si se recibe 0 y AB debería indicar que son compatibles y AB es receptor de 0.
'''
'''
grupoSanguineo1 = input("Dime un grupo sanguineo:")
grupoSanguineo2 = input("Dime un grupo sanguineo:")


if (grupoSanguineo1 == "A" or grupoSanguineo1 == "B" or grupoSanguineo1 == "AB" or grupoSanguineo1 == "0") and (grupoSanguineo2 == "A" or grupoSanguineo2 == "B" or grupoSanguineo2 == "AB" or grupoSanguineo2 == "0"):
    
    if grupoSanguineo1 == "A" and grupoSanguineo2 == "A":
        print("Ambos grupos sangineos son compatibles, A puede donar a: A y A puede recibir de: A.")
    
    elif grupoSanguineo1 == "A" and grupoSanguineo2 == "B":
        print("Ambos grupos sangineos no son compatibles.")
    
    elif grupoSanguineo1 == "A" and grupoSanguineo2 == "AB":
        print("Ambos grupos sangineos son compatibles, A puede donar a: AB y AB puede recibir de: A")    
    
    elif grupoSanguineo1 == "A" and grupoSanguineo2 == "0":
        print("Ambos grupos sangineos son compatibles, 0 puede donar a: A y A puede recibir de: 0")
    
    elif grupoSanguineo1 == "B" and grupoSanguineo2 == "B":
        print("Ambos grupos sangineos son compatibles, B puede donar a: B y B puede recibir de: B")
    
    elif grupoSanguineo1 == "B" and grupoSanguineo2 == "AB":
        print("Ambos grupos sangineos son compatibles, B puede donar a: AB y AB puede recibir de: B")
    
    elif grupoSanguineo1 == "B" and grupoSanguineo2 == "0":
        print("Ambos grupos sangineos son compatibles, 0 puede donar a: B y B puede recibir de: 0")
    
    elif grupoSanguineo1 == "AB" and grupoSanguineo2 == "AB":
        print("Ambos grupos sangineos son compatibles, AB puede donar a: AB y AB puede recibir de: AB")
        
    elif grupoSanguineo1 == "AB" and grupoSanguineo2 == "0":
        print("Ambos grupos sangineos son compatibles, 0 puede donar a: AB y AB puede recibir de: 0")
    
    elif grupoSanguineo1 == "0" and grupoSanguineo2 == "0":
        print("Ambos grupos sangineos son compatibles, 0 puede donar a: 0 y 0 puede recibir de: 0")
'''