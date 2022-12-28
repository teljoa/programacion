'''
4. Función tal que dadas las coordenadas de un triángulo en el plano, nos devuelve
su perímetro
'''
def perimetro_equilatero(l):
    perimetro = l*3
    return perimetro

def perimetro_isoceles(l,b):
    perimetro = 2*l+b
    return perimetro

def perimetro_escaleno(a,b,c):
    perimetro = a+b+c
    return perimetro

print(perimetro_equilatero(4))
print(perimetro_isoceles(4,7))
print(perimetro_escaleno(2,6,8))
