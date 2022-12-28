'''
3. Write a Python program to get the least common multiple (LCM) of two positive
integers.
'''

def gcd(a, b):
    if a == 0:
        return b
    
    return gcd(b % a, a)


def lcm(a, b):
    return (a / gcd(a, b)) * b


if __name__ == '__main__':
    print("LCM = ", lcm(4, 6))