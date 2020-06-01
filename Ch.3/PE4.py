# Roman Numberals

num = int(input('Enter in a number between 1-10: '))

if num < 1 or num > 10:
    num = int(input('Error: Please re-enter in a number between 1-10: '))
if num == 1:
    print('Number', num, 'is I')

elif num == 2:
    print('Number', num, 'is II')

elif num == 3:
    print('Number', num, 'is III')

elif num == 4:
    print('Number', num, 'is IV')

elif num == 5:
    print('Number', num, 'is V')

elif num == 6:
    print('Number', num, 'is VI')

elif num == 7:
    print('Number', num, 'is VII')

elif num == 8:
    print('Number', num, 'is VIII')

elif num == 9:
    print('Number', num, 'is IX')

else:
    print('Number', num, 'is X')
