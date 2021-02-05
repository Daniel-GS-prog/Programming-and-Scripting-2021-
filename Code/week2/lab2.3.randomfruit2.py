# Takes a random fruit from a list
# Author: Daniel Gonzalez

import random

 ## -- List of fruits to randomly select on3 --##
fuits = ('banana', 'mango', 'pear', 'blueberries', 'strawberries', 'tomatoe')

## -- Makes a radon choice from the list -- ##
randomFruit = random.choice(fuits)

## -- Prints the result -- ##
print('A random fruit: {}'.format(randomFruit))
