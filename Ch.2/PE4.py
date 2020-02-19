# Chapter 1
# Program 4
# Algorithm
# 1. Ask the user to enter the prices of 5 items
# 2. User enters in the items
# 3. Add all the items to get subtotal
# 4. Multiply subtotal by sales_tax to get salesTax
# 5. Add tje salesTax and subtotal to get the final total
# 6. Display results

# Variables
sales_tax = 0.07

# Ask for user input
print("\nEnter in the 5 items below")

# User input
item1 = float(input("Enter price of item 1: $"))
item2 = float(input("Enter price of item 2: $"))
item3 = float(input("Enter price of item 3: $"))
item4 = float(input("Enter price of item 4: $"))
item5 = float(input("Enter price of item 5: $"))

# Calculations
subtotal = item1+item2+item3+item4+item5
salesTax = subtotal * sales_tax
total = subtotal + salesTax

# Display results
print("\nSubtotal:  $", subtotal)
print("Sales Tax: $", salesTax)
print("Total:     $", total)
