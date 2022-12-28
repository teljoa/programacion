'''Entrega de 28 de Octubre'''

cantidad = int(input("Dime cuantas cifras quieres de Fibonachi que se muestren:"))

primerresutado=0

segundoresultado=1

suma=0

count=1

print("secuencia de Fibonachi: ")


while(count<=cantidad):    
    print(suma)
    count+=1
    primerresultado=segundoresultado
    segundoresultado=suma
    suma=primerresultado+segundoresultado    
