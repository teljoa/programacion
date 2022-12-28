'''
1. Design a function called charactersInString that has a character string and a character as
input parameters and returns how many times that character appears in the string. It should
do if the string and character are lower case or upper case characters.
'''
chp ="hsgshfksdklfjhweiojhvksdllke".upper()
l = "d".upper()

def charactersInString(chp,l):
    np = 0
    for i in chp:
        if l == i:
            np+=1
    return np

print(charactersInString(chp,l))