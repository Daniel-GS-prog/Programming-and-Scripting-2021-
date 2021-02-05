# Final questions from lab2.3
#Author: Daniel Gonzalez



## -- 1 -- ##
# Why does this expression cause an error? How can you fix it? 
# message = 'I have eaten ' + 99 + ' burritos.'
# print (message)
# There's a mixture of str and int. For a proper print 99 needs to be turned into a str

message = 'I have eaten ' + str(99) + ' burritos.'
print (message)
## ------ ##

## -- 2 -- ##
# Why is eggs a valid variable name while 100 is invalid? 
# Rs: variables cannot start with numbers


## -- 3 -- ##
# What three functions can be used to get the integer, floating-point number, or
# string version of a value?
number = 12
print(float(number))
print(str(number))
print(int(number))