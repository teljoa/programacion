'''
5. Design a method called powerIt that receives two integers and raises the first
number to the second. You may use the product or recursion and check the values. If
no exponent is provided the first number is raised to 0
'''

num1 = 4
num2 = 6

def powerIt(num1,num2):
    if num2 in []:
        power = 0
    else:
        power = num1**num2
        
    return power

print(powerIt(num1,num2))