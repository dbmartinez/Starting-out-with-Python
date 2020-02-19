#Chapter 1
#Program 2
# Algorithm
# 1. Obtain user input
# 2. calculate profit
# 3. profit = total_tax * tax
# 4. display profit
# 5. display total sales

#variables
tax = 0.23

#User input
total_sales = (float(input("\nEnter in total sales: $")))

profit = float(total_sales * tax)

print("\nTotal sales: $", total_sales)
print("Profit from Total Sales: $", profit)