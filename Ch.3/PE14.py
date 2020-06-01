# Body Mass Index

weight = float(input('Enter in your weight: '))

height = float(input('Enter in you height(inches): '))

BMI = weight * 703/(height**2)

print('\nYour Body Mass Index(BMI) is: ', format(BMI, '.2f'))

if BMI < 18.5:
    print('You\'re considered to be underweight.')

elif BMI > 25:
    print('You\'re considered to be overweight')

else:
    print('Your weight is in great shape')