'''
4. Write a Python program that accepts two integers (n and i) and computes the value
of n+nn+nnn+.... 

n = 2, i = 3
result = 2 + 22 + 222 = 246

n = 1, i = 5
result = 1 + 11 + 111 + 1111+ 11111 = 12345
'''


n, m = 1, 5

change = n

s = 0

for i in range(m):
    s += change
    change = change * 10 + n

print(s)