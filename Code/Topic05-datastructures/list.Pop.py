# Creates a list of 10 random numbers, 
# selects the first one and the remainder list.
# then it deletes that first number
# Author: Daniel Gonzalez

import random

list = []
#List to be populated with for loop

for i in range (0, 10):
    # Range of the desired lenght of list
    n = random.randint(1, 100)
    # Random number for list
    list.append(n)
    # Number added to list


print('Qeue is {}.'.format(list))
    # First list 

for i in range(10):
    print('Current number is {} and the queue is'.format(list[0]), end="")
    # Selects first number of the list
    list.pop(0)
    # Deletes first number of list
    print(list)
    # prints remainder list
    if len(list) == 0:
    # Last statment
        print('the queue is now empty')    

    

