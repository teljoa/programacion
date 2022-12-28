'''
4. Design a function called numberInString that has a string of characters as parameter, the
method should return how many of those characters are numbers.
'''
chp ="hsgs7hfksdk75lFjhwe754ioJhvkS6354dllke"

def lowCaseInString(chp):
    lcm = 0
    for i in chp:
        if i.isnumeric():
            lcm+=1
    return lcm

print(lowCaseInString(chp))