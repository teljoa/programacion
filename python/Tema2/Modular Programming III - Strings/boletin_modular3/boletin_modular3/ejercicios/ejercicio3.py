'''
3. Design a function called upperCaseInString that has a string of characters as parameter, the
method should return how many of those characters are upper case letters.
'''
chp ="hsgshfksdklFjhweioJhvkSdllke"

def lowCaseInString(chp):
    lcm = 0
    for i in chp:
        if i.isupper():
            lcm+=1
    return lcm

print(lowCaseInString(chp))