# Age Classifier

age = int(input('Enter in person\'s age: '))

if age <= 1:
    print('He/she is an infant')

elif age > 1 and age <= 13:
    print('He/she is a child')

elif age > 13 and age <= 20:
    print('He/she is a teenager')

else:
    print('He/she is an adult')
