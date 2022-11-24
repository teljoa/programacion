'''
9. Design a method called getPrimeDivisors that receives a positive number as a
parameter and returns a list containing its prime divisors. If the parameter is not valid
the method should return None.
'''

def isPrime(n):
    isPrime = True
    
    for i in range(2,n):
        if n%i==0:
            isPrime = False
            
    return isPrime

def getPrimeDivisors(n):
    getPrimeDivisors = []
    for i in range(n):
        if isPrime(i) == True:
            getPrimeDivisors.append(i)
    
    return getPrimeDivisors

n = 46

print(getPrimeDivisors(n))