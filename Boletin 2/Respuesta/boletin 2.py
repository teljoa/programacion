'''
Escribir una expresión lógica que cumpla:
'''

#a) Debe ser Verdadera si el contenido de las variables enteras sueldo_bruto y sueldo_neto es el 
#adecuado para una retención del 22%.
salariobruto = 1000
salarioneto = 780
print(salariobruto*(1 - 0.22)== salarioneto)
#b) Debe ser Verdadera si el contenido de la variable entera día es un valor válido para el mes 
#de mayo.
mes = 'mayo'
dia = 26
print(mes == 'mayo',  dia <= 31 and dia >= 1)
#c) Debe ser Verdadera si el número contenido en las variables enteras num1 y num2 son múltiplos 
#de tres.
numero1 = 14
numero2 = 20 
print(not(numero1 % 3 ==0 and numero2 % 3 ==0))
#d) Debe ser Verdadera si la calificación contenida en la variable real nota es un aprobado.
nota = 8
print(nota <= 5 and nota <= 10)
#e) Debe ser Verdadera si la media de la calificación contenida en las variables reales nota1, 
#nota2 y nota3 es un aproblado.
nota1 =  7
nota2 =  2
nota3 =  5
print(nota1 + nota2 + nota3 % 2 >= 5)
'''
Escribir una expresión lógica que cumpla:
'''

#a) Debe ser Falsa si alguna de las calificaciones contenidas en las variables reales nota1, 
#nota2 y nota3 es un suspenso.
nota1 =  7
nota2 =  2
nota3 =  5
print(nota1 >= 5 and nota2 >= 5 and nota3 >= 5)
#b) Debe ser Falsa si la persona no es un usuario fiable, esto ocurrirá cuando tenga menos de 
#1000 euros en la variable saldo o se haya quedado al descubierto más de 5 veces. Este último 
#dato se almacenará en la variable descubierto.
descubierto = 6
saldo = 1500
print(not(saldo >= 1000 or descubierto < 5))
#c) Debe ser Falsa cuando el valor almacenado en la variable asignaturasAprobadas sea inferior al
#30% del valor almacenado en la variable asignaturasCurso.
asignaturaaprobadas = 5
asignaturacurso = 7
print(not(asignaturacurso*(1 - 0,30) == asignaturaaprobadas))
#d) Debe ser Falsa si los números contenido en las variables enteras mes y día no son válidos. 
#Vamos a considerar que no hay años bisiestos.

mes = 6
dia = 28
print(not((mes == 1 or mes ==3 or mes ==7 or mes ==8 or mes == 10 or mes ==12 and dia >= 1 and dia <=31) or (mes == 4 or mes == 6 or mes ==9 or mes ==11 and dia >= 1 and dia <= 30) or (mes == 2 and dia >= 1 and dia <= 28)))

