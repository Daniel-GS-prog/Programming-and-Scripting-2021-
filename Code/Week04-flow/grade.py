# reads in a percentage mark an prints out corresponding the grade
# Author: Daniel Gonzalez


studentPercentage = float(input('please enter your mark: '))


## -- Checks value is a valid percentage:
if studentPercentage < 0 or studentPercentage > 100:
    print('value should be between 0 and 100')

## -- Comparison:   
else:
    if studentPercentage <= 40:
        print('fail mark.')
    elif 40 <= studentPercentage <= 49:
        print('Pass mark')
    elif 50 <= studentPercentage <= 59:
        print('Merit 2 mark')
    elif 60 <= studentPercentage <= 69:
        print('Merit 1 mark')
    else:
        print('Distinction!')