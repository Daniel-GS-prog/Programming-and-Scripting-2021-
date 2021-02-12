# asks the user to enter in a number and says if it's even or odd
# Author: Daniel Gonzalez

number = int(input('Please enter a number: '))


if number % 2 == 0: # even division will have 0 as remainder. 
    print('{} is an even number.'.format(number))
else:
    print('{} is an odd number.'.format(number))

