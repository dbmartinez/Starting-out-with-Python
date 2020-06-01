#Software Sales

package_retail = 99

print('Price per package is $', package_retail, sep='')
quantity = int(input('Enter in the number of packages purchased: '))

if quantity < 0:
    print('Error: can\'t enter a negative number')
    quantity = int(input('Enter in the number of packages purchased: '))

total = quantity * package_retail

if  quantity >= 0 and quantity <= 9:
    total = quantity * package_retail
    discount = 0

elif quantity >= 10 and quantity <= 19:
    print('\nCongratulations, you qualify for a 10% discount')
    discount = total * 0.1

elif quantity >= 20 and quantity <= 49:
    print('\nCongratulations, you qualify for a 20% discount')
    discount = total * 0.2

elif quantity >= 50 and quantity <= 99:
    print('\nCongratulations, you qualify for a 30% discount')
    discount = total * 0.3

elif quantity >= 100:
    print('\nCongratulations, you qualify for a 40% discount')
    discount = total * 0.4

new_total = total - discount
print('\nSales information')
print('-----------------')
print('Amount: $', format(total, ',.2f'), sep='')
print('Discount amount: $', format(discount, ',.2f'), sep='')
print('Total amount: $', format(new_total, ',.2f'), sep='')