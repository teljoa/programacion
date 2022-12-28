'''
5. Queremos crear un programa que trabaje con fracciones de la forma a/b. Para
representar una fracción vamos a utilizar dos enteros: numerador y denominador,
creando las siguientes funciones para trabajar con ellas:

i. leer_fracción: La tarea de esta función es leer por teclado el numerador y el
denominador y la devuelve simplificada (Por ejemplo, si recibe 16/6 ⇒ 8/3).

ii. escribir_fracción: muestra por pantalla la fracción; si el denominador es 1, se
muestra sólo el numerador.

iii. calcular_mcd: Esta función recibe dos números y devuelve su máximo común
divisor.

iv. simplificar_fracción: simplifica una fracción. Para ello hay que dividir el
numerador y denominador por su MCD.

v. sumar_fracciones: recibe dos funciones n1/d1 y n2/d2 y calcula su suma. La
suma de dos fracciones es otra fracción cuyo numerador n=n1*d2+d1*n2 y
denominador d=d1*d2, simplificando la fracción resultado.

vi. restar_fracciones: resta dos fracciones, siendo el numerador de la resta
n=n1*d2-d1*n2 y el denominador d=d1*d2, simplificando el resultado.

vii. multiplicar_fracciones: recibe dos fracciones y calcula su producto, siendo el
numerador del producto n=n1*n2 y el denominador d=d1*d2 (simplificando).

viii. dividir_fracciones: calcula el cociente de dos fracciones, siendo el numerador
n=n1*d2 y denominador d=d1*n2 (simplificando el resultado).
'''

def leer_fraccion(nud,dmd):
    resultado = (nud//2) and (dmd//2)
    return resultado

def escribir_fraccion(nud,dmd):
    fraccion = []
    if dmd == 1:
        fraccion.append(nud)
    else:
        fraccion.append([nud, dmd])
    return fraccion

def calcular_mcd(nud,dmd):
    tml = 0
    while dmd != 0:
        tml = dmd
        dmd = nud % dmd
        nud = tml
    return nud

def simplificar_fracción(nud,dmd):
    resultado=calcular_mcd(nud,dmd)//nud,dmd
    return resultado

def sumar_fracciones(nud1,dmd1,nud2,dmd2):
    nud=(nud1*dmd2)+(dmd1*nud2)
    dmd=dmd1*dmd2
    return nud,dmd

def restar_fracciones(nud1,dmd1,nud2,dmd2):
    nud=nud1*dmd2-dmd1*nud2
    dmd=dmd1*dmd2
    return nud,dmd

def multiplicar_fracciones(nud1,dmd1,nud2,dmd2):
    nud=nud1*nud2
    dmd=dmd1*dmd2
    return nud,dmd
def dividir_fracciones(nud1,dmd1,nud2,dmd2):
    nud=nud1*dmd2
    dmd=dmd1*nud2
    return nud,dmd

print(leer_fraccion(4,2))
print(escribir_fraccion(4,2))
print(calcular_mcd(4,2))
print(simplificar_fracción(4,2))
print(sumar_fracciones(4,2,4,2))
print(restar_fracciones(4,2,4,2))
print(multiplicar_fracciones(4,2,4,2))
print(dividir_fracciones(4,2,4,2))
