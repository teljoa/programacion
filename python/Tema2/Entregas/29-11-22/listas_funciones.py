'''
Funcion usuario
'''

def generar_usuario(nombre,apellido1,apellido2,dni):
    usuario=[]
    usuario = nombre[0]+nombre[1]+nombre[2]+apellido1[-1]+apellido1[-2]+apellido1[-3]+apellido2[0]+apellido2[1]+apellido2[2]+dni[-2]+dni[-3]+dni[-4]+dni[-5]
    return usuario

'''
1.
'''
opcion =0
while opcion < 6:
    print("1.Añadir usuario valido")
    print("2.Eliminar usuario")
    print("3.Crear usuario")
    print("4.consultar usuarios")
    print("5.Borrar usuarios")
    print("6.Salir")
    opcion = input("Eliga una opcion:")
    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass  
    elif opcion == 5:
        pass
    else:
        None
    