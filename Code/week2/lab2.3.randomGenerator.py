# Prints a random number between 1 and 10
# Author: Daniel Gonzalez

import random


## -- asks the user for two numbers (range) for a random selection -- ##
print(
    '\nWelcome, you will be asked for two numbers.\n'
    'Those two numbers will generate a range and a random number will be selected.\n')

number1 = int(input('Please enter your firs inferior number: '))
number2 = int(input('Please enter your second superior number: '))


## -- generates a random number from the range provided by the user --##
randomNumber = random.randint(number1, number2) 


## -- Prints the selected random number -- ##
print('This is a random number between {} and {}: {}.'.format(number1, number2, randomNumber)) 