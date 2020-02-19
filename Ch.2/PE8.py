# Chapter 2
# Program 8
# Algorithm
# 1. Ask user to enter charge
# 2. Calculate 7 percent sales tax
# 3. Calculate 18 percent tip
# 4. Display each amount and total

# Variables
sTax = 0.07
tip = 0.18

# User input
food_charge = float(input("\nEnter in the cost of the meal: $"))

# Calculations
newTip = tip * food_charge
newTax = sTax * food_charge
total = newTax + newTip + food_charge

# Results
print("\nMeal Cost:    $", food_charge)
print("Sales Tax:    $", newTax)
print("Gratuity:     $", newTip)
print("Total:        $", total)