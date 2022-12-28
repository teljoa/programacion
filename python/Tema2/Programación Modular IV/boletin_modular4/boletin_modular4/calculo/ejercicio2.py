'''
2. Write a Python program to compute the greatest common divisor (GCD) of two
positive integers.
'''

def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

print( maximo_comun_divisor(2, 22))