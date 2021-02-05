# Reads in two numbers and substracts the first one from the second one
# Author: Daniel Gonzalez


## -- Asks user for numbers –– ##

number1 = input('Please enter your first integer: ')
number2 = input('Please enter your second integer: ')
number3 = int(number1) - int(number2) # Converts the variables from str to int


## -- Returs the result –– ##

print('{} minus {} is {}.'.format(number1, number2, number3))
