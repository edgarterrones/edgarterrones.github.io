# Edgar C Terrones
# 10/7/25
# P2HW1
# Travel 2

# This saves users budget
print("Please enter your travel budget:")
budget = float(input())

# This saves users travel location
print("Please enter your travel destination:")
location = input()
# This saves how much you will spend on gas
print("How much will you spend on gas:")
gas = float(input())
# This saves how much you will spend on gas
print("How much will you spend on accomadation:")
hotel = float(input())
# This saves how much you will spend on food
print("How much will you spend on food:")
food = float(input())

# This will give you total expenses based on the information inputed
total = gas + hotel + food
print("Total Expenses = ",f"${total:.2f}")
# This subtracts your travel budge by your total expected cost in order to provide your remaining budget
remaining = budget - total

#This will print out a list of total expenses and remaining balance
print("--------Total Expenses--------")
print(f"{"Location:":<20}{location}")
print(f"{"Initial Budget:":<20}${budget:.2f}")
print(f"{"Fuel:":<20}${gas:.2f}")
print(f"{"Accomadation:":<20}${hotel:.2f}")
print(f"{"Food:":<20}${food:.2f}")



print(f"{"Remaining Balance:":<20}${remaining:.2f}")
print("------------------------------")
