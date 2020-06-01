# Mass and Weight

mass = int(input('Enter in object\'s mass: '))

if mass < 1:
    mass = int(input('Error: Please re-enter in object\'s mass: '))

weight = mass * 9.8

if weight >= 500:
    print('Weight is', format(weight, '.2f'), 'and is to heavy.')

elif weight <= 100:
    print('Weight is', format(weight, '.2f'), 'and is too light.')

else:
    print('Weight is', format(weight, '.2f'))
