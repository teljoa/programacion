'''
3. Realiza un programa que solicite la fecha como tres datos numéricos (día, mes y
año) y muestre a continuación la fecha en formato largo.
Introduce el día de la fecha: 15
Introduce el mes de a fecha: 3
Introduce el año de a fecha: 2009
La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo.
'''
dia = 15
mes = 3
agno = 2022

meses = ['enero','febrero','marzo','abril','mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre','diciembre']

def listaDiasAgno(agno):
    
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    
    if ( (agno % 4 == 0 and agno % 100 != 0) or (agno % 400 == 0) ):
        dias[1]=29
    return dias

while ( not(0 < mes <= 12) and (mes > 0) ):
    mes = input(' Mes no valido, pruebe de nuevo')

if mes > 0:
    while ( not(0 < mes <= 12) and (mes > 0) ):
        mes = input(' Año no valido, pruebe de nuevo')   
    
    else:
        while dia > listaDiasAgno(agno)[mes+1]:
            dia = input(' Dia no valido, pruebe de nuevo')
            