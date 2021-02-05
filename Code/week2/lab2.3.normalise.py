# Reads in a string and strips any leading. Also convert the string to lower case. 
# Author: Daniel Gonzalez


## -- Askes the user for a string -- ##
string = input("Please enter your string: ")


## -- Normalisation of the string -- ##
strippedString = string.strip() #- strips the string
normalisedString = strippedString.lower() #- Turns string into lowercase


## -- Determines both strings' length -- ##
stringLength = len(string)
normalisedStringLenght = len(normalisedString)


## -- Prints the resulting string --##
print('\nThat string noemalised is: {}.'.format(normalisedString))
print('We reduced the input from {} to {} characters.'.format(stringLength, normalisedStringLenght))

