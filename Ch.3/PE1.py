# Day of the Week

day = int(input('\nEnter in a number between 1 and 7: '))

if day < 1 or day > 7:
    day = int(input('\nError: Please re-enter in a number between 1 and 7: '))

if day == 1:
    print('It\'s Monday')

elif day == 2:
    print('It\'s Tuesday')

elif day == 3:
    print('It\'s Wednesday')

elif day == 4:
    print('It\'s Thursday')

elif day == 5:
    print('It\'s Friday')

elif day == 6:
    print('It\'s Saturday')

else:
    print('It\'s Sunday')
