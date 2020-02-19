# Chapter 1
# Program 2
# Algorithm
# 1. Ask user to enter total square feet
# 2. Calculate number of acres
# 3. Divide the amount entered by 43,560 to get the number of acres
# 4. Display total square feet
# 5. Display amount of acres

# Variables
one_acre = 43560

total_square_feet = int(input("\nEnter in total square feet of tract of land: "))

# Calculation
total = total_square_feet // one_acre

# Display information
print("\nTotal Square feet: ", total_square_feet)
print("Number of acres: ", total)
