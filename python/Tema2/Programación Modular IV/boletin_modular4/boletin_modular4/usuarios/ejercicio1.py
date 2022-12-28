'''
1. Diseña un programa que permite guardar el nombre de usuario y contraseña de
hasta 10 usuarios diferentes. Si el usuario ya existe en el sistema, puede hacer
login tras incluir un usuario y contraseña válidas hasta un máximo de tres
intentos, momento en el que se bloquea su cuenta.

Si el usuario no existe, puede crear una cuenta siempre que haya espacio
(máximo 10), para lo que se le pedirá usuario y contraseña, así como la
confirmación de ésta última.

El menú de este programa permitirá identificarse y crear cuentas nuevas, así
como mostrar todos los nombres de usuario existentes sin sus contraseñas.
'''

usuarios = []
contrasenas = []
intentos = 0
usuario = ""
contrasena =""
opcion = 0
while opcion < 4:
    print("Menu")
    print("1.Crear usuario")
    print("2.Entrar")
    print("3.Ver usuarios exixtentes")
    print("4.Salir")
    opcion = int(input("Elige una opcion:"))
    if opcion == 1:
        if len(usuarios) <=9:
            usuario=input("Introduce un usuario valido:")
            contrasena=input("Introduce una contraseña valida:")
            if usuario not in usuarios:
                usuarios.append(usuario)
            if contrasena not in contrasenas:
                contrasenas.append(contrasena)
    elif opcion ==2:
        while intentos !=3:
            usuario = input("Introduce tu usuario:")
            contrasena = input("Introduce tu contrseña:")
            if (usuario not in usuarios) and (contrasena not in contrasenas):
                intentos+=1
            elif (usuario in usuarios) and (contrasena in contrasenas):
                pass
    elif opcion ==3:
        print(usuarios)