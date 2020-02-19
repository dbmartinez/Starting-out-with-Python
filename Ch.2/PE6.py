# Chapter 2
# Program 6
# Algorithm
# 1. Ask user to enter amount of purchase
# 2. Calculate and add the state and county taxes
# 3. Add the taxes and purchase together to get total
# 4. Display results

# Variables
county_tax = 0.025
state_tax = 0.05

# User input
purchase = float(input("\nEnter in the cost of purchase: $"))

# Calculations
new_countyTax = county_tax * 100
new_stateTax = state_tax * 100
total_salesTax = new_stateTax + new_countyTax
total = total_salesTax + purchase

# Display results
print("\nAmount of purchase:     $", purchase)
print("County sales tax:       $", new_countyTax)
print("State sales tax:        $", new_stateTax)
print("Total sales tax:        $", total_salesTax)
print("Total cost of purchase: $", total)