# reads in a percentage mark an prints out corresponding the grade
# Author: Daniel Gonzalez


studentPercentage = float(input('please enter your mark: '))


## -- Comparison:
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