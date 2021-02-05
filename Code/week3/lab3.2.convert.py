 # takes in a float amount of dollars, and returns that absolute amount in cent
 # Author: Daniel Gonzalez


## -- Asks the user to enter an amount to convert -- ##
amount = float(input('Please enter the amount: '))

## -- Converts that amount to an absolute value -- ##
absolute = abs(amount)

## -- Makes sure that value has two decimal points -- ##
limiteAmount = '{:.2f}'.format(absolute)

## -- Converts the amount into cents -- ##
cents = float(limiteAmount) * 100

## -- Returns the result -- ##
print('The amount in cents is= {}.'.format(cents))
