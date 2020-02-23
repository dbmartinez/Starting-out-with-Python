# Chapter 2
# Program 11
# Algorithm
# 1. Ask user input
# 2. Calculate percentage of male and females
# 3. Display results

# User input
male = int(input("\nHow many males are registered in the class: "))
female = int(input("How many females are registered in the class: "))

# Calculations
total = male + female
malesPercent = male / total
femalesPercent = female / total

# Display results
print("\nPercentage of males: ", malesPercent * 100, "%")
print("Percentage of females: ", femalesPercent * 100, "%")