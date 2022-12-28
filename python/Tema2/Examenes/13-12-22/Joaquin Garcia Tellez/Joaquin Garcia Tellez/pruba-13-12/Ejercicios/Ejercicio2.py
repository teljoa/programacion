def dame_numero():
    from random import randint
    return randint(2,12)

opcion =0
saldot=float(input("Introduzca con cuanto saldo quiere empezar(€):"))
while opcion !=4 or saldot==0:
    print("Menu")
    print("###################################################")
    print("1.Apostar:Seleciona el numero y cantidad a apostar")
    print("2.Añadir mas saldo: introducir saldo a incrementar.")
    print("3.Mostrar saldo")
    print("4.Retirarse")
    
    opcion=int(input("Introduzca que opcion quiere realizar:"))
    if opcion ==1:
        numero=int(input("Introduzca el numero por el que quiere apostar:"))
        apuesta=float(input("Introduzca la cantidad(€) que quiere apostar: "))
        if numero == dame_numero():
            saldog = apuesta*2
        elif numero < dame_numero():
            saldog = apuesta/2
        elif numero > dame_numero():
            saldog = 0
        saldot = saldot + saldog
    elif opcion ==2:
        saldoa=float(input("Introdusca con cuanto saldo(€) quiere añadir:"))
        saldot = saldoa + saldot
    elif opcion ==3:
        print(saldot)
    else:
        None