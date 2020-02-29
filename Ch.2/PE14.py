# Chapter 2
# Program 14
# Algorithm
# 1. Ask for user input
# 2. Calculate user input
# 3. Display results

# User input
P = float(input("\nEnter in original deposit: "))
r = float(input("Enter in annual rate: "))
n = int(input("Enter in the amount of years interest compounded(monthly - 12, quarterly = 4): "))
t = int(input("Enter in the number of years: "))

# Calculations
A = P * (1 + ( r * .01 / n))**(n*t)

# Display Results
print("\nAmount: $", round(A, 2))