'''
2. Design a function called lowCaseInString that has a string of characters as parameter, the
method should return how many of those characters are lowcase letters.
'''
chp ="hsgshfksdklfjhweiojhvksdllke"

def lowCaseInString(chp):
    lcm = 0
    for i in chp:
        if i.islower():
            lcm+=1
    return lcm

print(lowCaseInString(chp))