#Money Counting Game

pennies = float(input('Enter in the amount of pennies: '))
if pennies < 0:
    print('Error: Can\'t be a negative number.')
    pennies = float(input('Enter in the amount of pennies: '))

nickels = float(input('Enter in the amount of nickels: '))
if nickels < 0:
    print('Error: Can\'t be a negative number.')
    nickels = float(input('Enter in the amount of nickels: '))

dimes = float(input('Enter in the amount of dimes: '))
if dimes < 0:
    print('Error: Can\'t be a negative number.')
    dimes = float(input('Enter in the amount of dimes: '))

quarters = float(input('Enter in the amount of quarters: '))
if nickels < 0:
    print('Error: Can\'t be a negative number.')
    quarters = float(input('Enter in the amount of quarters: '))

new_pennies = pennies * .01
new_nickels = nickels * .05
new_dimes = dimes * 0.1
new_quarters = quarters * 0.25

dollar = new_pennies + new_nickels + new_dimes + new_quarters

if dollar == 1:
    print('Congratulations, the amount equals a dollar.')

else:
    print('Sorry, the amount doesn\'t equal a dollar.')