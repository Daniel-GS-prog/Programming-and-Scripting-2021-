# generates 10 random numbers (0-100). prints them out then prints out the top three.
# Author: Daniel Gonzalez

import random


## -- 1. Generates a list of 1o random numbers between 1 and 100.
count = 0
numbers = []

while count < 10:
    numbers.append(random.randint(1,101))
    count += 1
print('ten randoms numbers = {}'.format(numbers))


## -- Sorts that list and prints out the top 3 numbers
sorterdNumbers = sorted(numbers, reverse=True)
i = 0
n = 0
sortedList = []
while i < 3:
    sortedList.append(sorterdNumbers[n])
    n += 1
    i += 1
print('Top Thre are: {}.'.format(sortedList))