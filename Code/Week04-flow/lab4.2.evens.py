# print all the even numbers from 2 to 100.
# Author: Daniel Gonzalez


top = 100
start = 0

while start <= top:
    if start % 2 == 0: # even number divided by 2 have no remainder
        print(start)
    start += 1
    
