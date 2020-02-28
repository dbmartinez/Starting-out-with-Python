# Chapter 2
# Program 13
# Algorithm
# 1. Ask for user input
# 2. Calculate user input
# 3. Display results

# User input
print("\nEnter information in feet")
R = float(input("\nEnter length of the row(in feet): "))
E = float(input("Enter in the amount of space by end post: "))
S = float(input("Enter in the amount of space between vines: "))

# Calculations
V = (R - 2*E) / S

# Display results
print("\nNumber of grapevines that will fit in the row: ", V)