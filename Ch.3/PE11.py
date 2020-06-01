#Book Club Points

purchases = int(input('Enter in the number of books you purchased this month: '))

if purchases < 0:
    print('Error: can\'t be a negative number')
    purchases = int(input('Enter in the number of books you purchased this month: '))

if purchases >= 0 and purchases <= 1:
    print('You\'ve earned 0 points')

elif purchases >= 2 and purchases <= 3:
    print('You\'ve earned 5 points')

elif purchases >= 4 and purchases <= 5:
    print('You\'ve earned 15 points')

elif purchases >= 6 and purchases <= 7:
    print('You\'ve earned 30 points')

else:
    print('You\'ve earned 60 points')