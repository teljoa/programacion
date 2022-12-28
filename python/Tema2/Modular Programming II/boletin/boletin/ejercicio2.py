'''
2. Design a method called isLeapYear that receives a number and returns False for
common years and True for leap years. You may know that a year is considered to
be a leap year if it is divisible by 4, unless it is also divisible by 100. A year is not a
leap year if it is divisible by 100 unless it is also divisible by 400.
'''

def es_bisiesto(ayo):
    if ayo % 4 == 0 and (ayo % 100 != 0 or ayo % 400 == 0):
        ayo = True
    else:
        ayo = False
        
    return ayo

ayo = 2020

print(es_bisiesto(ayo))