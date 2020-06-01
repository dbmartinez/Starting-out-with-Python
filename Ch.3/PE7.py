# Color Mixer

color1 = input('Enter in first color: ')

if not (color1 == 'red' or color1 == 'yellow' or color1 == 'blue'):
    color1 = input('Error: Please re-enter in first color: ')

color2 = input('Enter in second color: ')

if not (color2 == 'red' or color2 == 'yellow' or color2 == 'blue'):
    color1 = input('Error: Please re-enter in second color: ')

if color1 == 'red' and color2 == 'yellow':
    print('Resulting color is orange')

elif color1 == 'red' and color2 == 'blue':
    print('Resulting color is purple')

elif color1 == 'blue' and color2 == 'yellow':
    print('Resulting color is green')

elif color2 == 'red' and color1 == 'yellow':
    print('Resulting color is orange')

elif color2 == 'red' and color1 == 'blue':
    print('Resulting color is purple')

elif color2 == 'blue' and color1 == 'yellow':
    print('Resulting color is green')
