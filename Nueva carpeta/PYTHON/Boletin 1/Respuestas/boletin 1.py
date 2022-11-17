'''
BOLETIN 1

Ejercicio 1
'''
#a) 7>=27 AND NOT (7<=2)
print(7>=27 and not(7<=2))#false
#b) 24>5 AND 10<=10 OR 10=5
print(24>5 and 10<=10 or 10==5)#true
#c) (10>=15 OR 23=13) AND NOT(8=8)
print((10>=15 or 23==13) and not(8==8))#false
#d) NOT (6/3>3) OR 7>7
print(not (6/3>3) or 7>7)#true

'''
Ejercicio 2
'''
#A)27 mod 4 + 15\4
print(27%4+15/4, type(27%4+15/4))
#B)37\4^2–2
print(37/4**2-2, type(37/4**2-2))
#C)9*2/3*10*3
print(9*2/3*10*3, type(9*2/3*10*3))
#D)(7*3–4*4)^2\4*2
print((7*3-4*4)**2/4*2, type((7*3-4*4)**2/4*2))
'''
3. Escribir una expresión lógica que cumpla:
'''
#a) Debe ser Verdadera si el contenido de la variable entera precio es igual o superior a 60 euros pero igual o inferior a 420 euros.
precio =60
print(60 <= precio and precio <= 420, 60<= precio <= 420)
#b) Debe ser Verdadera si el numero contenido en la variable entera numero es impar.
numero = 15
print(numero % 2 ==1)
#c) Debe ser Verdadera si las dos variables enteras saldo de una cuenta, y dineroSacar son válidas.
saldo = True
dinerosacar = True
print(saldo and dinerosacar)
#d) Debe ser Verdadera si las variables enteras hora y minutos son correctas, es decir, que estén comprendidas entre 0:0 y 23:59.
hora = 4
minuto = 45
print(hora >= 0 and hora <= 23, minuto >= 0 and minuto <= 59)
#e) Debe ser Verdadera si la variable estadoCivil que almacena el estado civil de una persona no es correcta (S-Soltero, C-Casado, V-Viudo, D-Divorciado).

estadocivil = 'S'

print(not(estadocivil == 'S' or  estadocivil == 'C' or estadocivil == 'V' or estadocivil =='D' ))

'''
4. Escribir una expresión lógica que cumpla:
'''

#a) Debe ser Falsa cuando la variable cantidad que contiene la cantidad a sacar de un cajero es superior a 300 euros o negativa.
cantidad = 500
print(cantidad <= 300 or cantidad >= 0)
#b) Debe ser Falsa si la persona es un adolescente, es decir, la variable edad está entre 16-22 años.
edad = 18
print(not(edad >= 16 and edad <= 22))
#c) Debe ser Falsa si la variable respuesta a una pregunta de tipo (S/N) es válida.
respuesta = 'S'
print(not(respuesta == 'S' or respuesta == 'N'))
#d) Debe ser Falsa si el número contenido en la variable entera numero es múltiplo de 7 o de 3.
numero = 14
print(not(numero % 3 ==0 or numero % 7 ==0))

'''
Ejercicio 5
'''

A =True
B =True
#A) (A OR B) AND NOT(A)
print((A or B) and not(A)) #False
#B) NOT (A OR B) AND B
print(not (A or B) and B) #False
#C) A OR NOT (B)
print(A or not (B)) #True
#D) NOT ((A AND B) AND (B OR A))
print(not ((A and B) and (B or A))) #False