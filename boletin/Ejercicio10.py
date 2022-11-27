
'''
10. Design a method called isFriendNumber that receives two positive numbers and
returns True if the numbers are friends, False otherwise. Two numbers are
considered to be friends if the sum of its divisors, except the given number, is equal
to the second and vice versa.
'''

import math

def sumofFactors(n):
    res = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        count = 0; curr_sum = 1; curr_term = 1
        while (n % i == 0):
            count += 1
            n = n // i
            curr_term *= i
            curr_sum += curr_term
        
        res *= curr_sum
    if (n >= 2):
        res *= (1 + n)

    return res

def gcd(a, b):

    if (a == 0):
        return b
    return gcd(b % a, a)

def isFriendNumber(n, m):
    sumFactors_n = sumofFactors(n)
    sumFactors_m = sumofFactors(m)
    gcd_n = gcd(n, sumFactors_n)
    gcd_m = gcd(m, sumFactors_m)
    
    if (n // gcd_n == m // gcd_m and
        sumFactors_n // gcd_n == sumFactors_m // gcd_m):
        return True

    else:
        return False

n = 24 
m = 42
if(isFriendNumber(n, m)):
    print("Yes")
else:
    print("No")
