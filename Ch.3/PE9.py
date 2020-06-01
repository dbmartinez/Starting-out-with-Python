#Roulette Wheel Colors

pocket_num = int(input('Enter in a pocket number: '))

if pocket_num < 1 or pocket_num > 36:
    print('Error: invalid entry')
    pocket_num = int(input('Please re-enter in a pocket number: '))

if pocket_num == 0:
    print('Green')

elif pocket_num >= 1 or pocket_num <= 10:
    if pocket_num == 1 or pocket_num == 3 or pocket_num == 5 or pocket_num == 7 or pocket_num == 9:
        print('Red')

    else:
        print('Black')

elif pocket_num >= 11 or pocket_num <= 18:
    if pocket_num == 11 or pocket_num == 13 or pocket_num == 15 or pocket_num == 17:
        print('Black')

    else:
        print('Red')

elif pocket_num >= 19 or pocket_num <= 28:
    if pocket_num == 19 or pocket_num == 21 or pocket_num == 23 or pocket_num == 25 or pocket_num == 27:
        print('Red')

    else:
        print('Black')

elif pocket_num >= 29 or pocket_num <= 36:
    if pocket_num == 29 or pocket_num == 31 or pocket_num == 33 or pocket_num == 35:
        print('Black')

    else:
        print('Red')