# Hot Dog Cookout Calculator

hot_dogs = 10
hotdog_buns = 8

people_attend = int(input('Enter in the number of people attending: '))

if people_attend < 1:
    print('Error: input must be more than 1')
    people_attend = int(input('Re-enter in the number of people attending: '))

hotdog_given = int(input('How many hot dogs will be given to each person: '))

if hotdog_given < 1:
    print('Error: input must be more than 1')
    hotdog_given = int(input('How many hot dogs will be given to each person: '))

result = people_attend * hotdog_given
result1 = result // hot_dogs
result2 = result // hotdog_buns
result3 = result % hot_dogs
result4 = result % hotdog_buns

print('\nMinimum number of packages for hot dogs needed: ', result1)
print('Minimum number of packages for hot dog buns needed: ', result2)
print('Hot dogs that will be left over: ', result3)
print('Hot dog buns that will be left over: ', result4)
