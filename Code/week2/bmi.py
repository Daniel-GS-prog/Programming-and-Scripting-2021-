#
# Takes the user´s height and weight and returs the body mass index
# Author: Daniel Gonzalez

print('Welcome to he BMI calculator!')

name = input('What´s your name: ')
print('Hello, {}. Nice to meet you!'. format(name))

#User´s values:
weight = float(input('Please enter your weight in kg: '))
height = float(input('Please enter your height in meters: '))
bmi = weight / (height**2)

#Returns user´s BMI:
print('Your Body Mass Index is: {}'. format(bmi))

#cathegories:
if bmi < 18.5:
    print('Your bmi is a little too low. Please go eat something.')
elif 18.5 <= bmi <= 24.9:
    print('Ypur bmi is at healthy levels! Congrats')
else:
    print('Your bmi is a bit too high.')
    