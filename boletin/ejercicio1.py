'''
1. Design a method called computeFactorial that receives a positive integer and
returns the factorial for that number. If the number is negative the method should
return None
'''
def factorial(num): 
    if num < 0: 
        print("Factorial of negative num does not exist")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

num =7

print("Factorial of",num,"is", factorial(num)) 