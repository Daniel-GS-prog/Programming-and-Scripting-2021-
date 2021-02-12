# asks the user for a number until they guess a secret number
# Author: Daniel Gonzalez
import random


print('\nGuess a number between 1 and 10\n')
# Just so we're not here forever

count = 0
secretNumber = random.randint(1,10) 
number = int(input('Please enter your number: '))

while number != secretNumber:
    print('Nop')
    if number < secretNumber:
        print('That`s too low')
    elif number > secretNumber:
        print('That`s too high')
    number = int(input('Plese try again: '))

print('excelent! {} is equal to {}.'.format(number, secretNumber))