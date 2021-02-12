#  keeps reading numbers until the user enters a 0.
#  append each of them into a list.
#  prints out each of the numbers entered and the average of them.


# Author: Daniel Gonzalez

number = int(input("\nPlease enter a number: ")) # User prompt

numbers = [] # Empty list to be populated from user input

average = 0 # will add the numbers added by user

while number != 0:
    numbers.append(number)  # list will append the number
    average += number       # the number will be added
    number = int(input('Please enter another number (0 to quit): '))

for element in numbers: # prints the list of numbers
    print(element)

print('the average is = {}.'.format(average)) # prints the average

