# Chapter 2
# Program 10
# Algorithm
# 1. Ask user how many cookies they want to make
# 2. Calculate how much sugar, butter, and flour is needed
# 3. Display results

# Variables
sugar = 1.5
butter = 1
flour = 2.75

# User input
cookies = float(input("\nHow many cookies would you like to make: "))

# Calculations
new_Sugar = cookies / sugar
new_Butter = cookies / butter
new_Flour = cookies / flour

# Display results
print("\nSugar needed: ", new_Sugar)
print("Butter needed: ", new_Butter)
print("Flour needed: ", new_Flour)