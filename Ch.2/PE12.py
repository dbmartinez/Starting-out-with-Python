# Chapter 2
# Program 12
# Algorithm
# 1. Write a program that displays the following information
# 2. The amount of money he paid for the stock
# 3. The amount of commission he paid his broker when he bought the stock
# 4. The amount for which he sold the stock
# 5. The amount of commission he paid his broker when he sold the stock
# 6. Display the amount of money that he had left when he sold the stock
#    and paid his broker(both times). If this amount is positive, than he
#    made a profit. If the amount is negative, the he lost money.

# Variables
stock_Purchased = 2000
purchased_perShare = 40
stock_perShare = 42.75

# Calculations
totalStock = stock_Purchased * purchased_perShare
paidBroker = totalStock * 0.03
totalStockSold = stock_perShare * stock_Purchased
paidBroker2 = totalStockSold * 0.03
total = (totalStockSold - totalStock) - (paidBroker + paidBroker2)

print("\nAmount paid for the stock:  $", totalStock)
print("Amount paid to broker:      $", paidBroker)
print("Amount the stock sold for:  $", totalStockSold)
print("Amount paid to broker:      $", paidBroker2)
print("Total:                      $", total)

