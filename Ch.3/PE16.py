# February Days

year = int(input('Enter a year: '))

days = year % 100

if days == 0:
    new_days = year % 400

    if new_days == 0:
        print('In',year,'February has 29 days.')

    else:
        print('In',year,'February has 28 days.')

else:
    print('In',year,'February has 28 days.')
