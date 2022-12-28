'''
6. Crear un programa que utilizando las funciones anteriores muestre el siguiente
menú:

a. Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el
resultado.

b. Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la
resta.

c. Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra el
producto.

d. Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la
cociente.

e. Salir
'''

opcion=0
nud1=4
nud2=4
dmd1=2
dmd2=2
while opcion !=6:
    print("Menu:")
    print("a. Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.")
    print("b. Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.")
    print("c. Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra el producto.")
    print("d. Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.")
    print("e. Salir")
    opcion= input("Elige una opcion:")
    
    if opcion=="a":
        nud=(nud1*dmd2)+(dmd1*nud2)
        dmd=dmd1*dmd2
        return nud,dmd

    elif opcion=="b":
        nud=nud1*dmd2-dmd1*nud2
        dmd=dmd1*dmd2
        return nud,dmd

    elif opcion=="c":
        nud=nud1*nud2
        dmd=dmd1*dmd2
        return nud,dmd
    elif opcion=="d":
        nud=nud1*dmd2
        dmd=dmd1*nud2
        return nud,dmd