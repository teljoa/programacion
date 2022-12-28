'''
7. Design a method called isPrime that receives one integer positive number greater
than 0 as parameter. The method should return True if the number is prime or False if
not prime. If the parameter is not valid the method should return None.
'''

n = 1

def isPrime(n):
    isPrime = True
    
    for i in range(2,n):
        if n%i==0:
            isPrime = False
            
    return isPrime
    
    
print(isPrime(n))
