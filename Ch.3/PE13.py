#Shipping Charges

ship_charge1 = 1.50
ship_charge2 = 3.00
ship_charge3 = 4.00
ship_charge4 = 4.75

weight = float(input('Enter in the weight of the package(lbs): '))

if weight > 0 and weight <= 2:
    print('\nRate for this weight is $1.50')
    new_weight = weight * ship_charge1

elif weight >= 3 and weight <= 5:
    print('\nRate for this weight is $3.00')
    new_weight = weight * ship_charge2

elif weight >= 6 and weight <= 9:
    print('\nRate for this weight is $4.00')
    new_weight = weight *ship_charge3

elif weight >= 10:
    print('\nRate for this weight is $4.75')
    new_weight = weight * ship_charge4

print('\nSales Information')
print('-----------------')
print('Weight entered: ', weight)
print('Shipping Charges: $',format(new_weight, ',.2f'), sep='')