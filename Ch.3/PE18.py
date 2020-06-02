# Restaurant Selector

user1 = input('Is anyone in your party a vegetarian: ')
user2 = input('Is anyone in your party a vegan: ')
user3 = input('Is anyone in your party gluten-free: ')

print('\nHere are your restaurant choices:')

if user1 == 'no' and user2 == 'no' and user3 == 'no':
    print('Joe\'s Gourmet Burgers')

elif user1 == 'yes' and user2 == 'yes' and user3 == 'yes':
    print('Corner Cafe')
    print('The Chef\'s Kitchen')

elif user1 == 'yes' and user2 == 'yes' and user3 == 'no':
    print('Corner Cafe')
    print('The Chef\'s Kitchen')

elif user1 == 'yes' and user2 == 'no' and user3 == 'yes':
    print('Main Street Pizza Company')
    print('Corner Cafe')
    print('The Chef\'s Kitchen')

elif user1 == 'yes' and user2 == 'no' and user3 == 'no':
    print('Mama\'s Fine Italian')
    print('Main Street Pizza Company')