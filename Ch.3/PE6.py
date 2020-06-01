# Magic Dates

month = int(input('Enter in the month in numeric form: '))
day = int(input('Enter in the day in numeric form: '))
year = int(input('Enter in the year in 2 digit numeric form: '))

yearResult = month * day

if year == yearResult:
    print('This date is magic.')

else:
    print('This date is not magic.')
