# Edgar C Terrones
# 09/23/25
# P1HW2
# Travel Budget

# This saves users budget
print("Please enter your travel budget:")
budget = int(input())
# This saves users travel location
print("Please enter your travel destination:")
location = input()
# This saves how much you will spend on gas
print("How much will you spend on gas:")
gas = int(input())
# This saves how much you will spend on gas
print("How much will you spend on accomadation:")
hotel = int(input())
# This saves how much you will spend on food
print("How much will you spend on food:")
food = int(input())

# This will give you total expenses based on the information inputed
total = gas + hotel + food
print("Total Expenses =", total)
# This subtracts your travel budge by your total expected cost in order to provide your remaining budget
remaining = budget - total

#This will print out a list of total expenses and remaining balance
print("-----Total Expenses-----")
print("Location:", location)
print("Initial Budget:", budget)
print("Fuel:", gas)
print("Accomadation:", hotel)
print("Food:", food)



print("Remaining Balance:", remaining)
