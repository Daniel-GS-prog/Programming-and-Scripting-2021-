# Takes two numbers and divides the first one by the second one. 
# Returs the integer result and the remainder

#Author: Daniel Gonazlez

## -- Asks user for the numbers -- ##

number1 = int(input('Please enter your first integer: '))
number2 = int(input('Please enter your second integer: '))


## -- Returns results -- ##

integerResult = number1 // number2  #- Resulting integer 
remainderResutt = number1 % number2 #- Resulting remainder


## -- Returns results –– ##

print('{} divided by {} is {} with remainder {}.'.format(number1, number2, integerResult, remainderResutt))