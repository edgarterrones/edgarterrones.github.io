# Edgar C Terrones
# 09/23/25
# P1HW2
# Travel Budget

print("Please enter your travel budget:")
budget = int(input())
print("Please enter your travel destination:")
location = input()
print("How much will you spend on gas:")
gas = int(input())
print("How much will you spend on accomadation:")
hotel = int(input())
print("How much will you spend on food:")
food = int(input())
total = gas + hotel + food
print("Total Expenses =", total)
remaining = budget - total


print("-----Total Expenses-----")
print("Location:", location)
print("Initial Budget:", budget)
print("Fuel:", gas)
print("Accomadation:", hotel)
print("Food:", food)



print("Remaining Balance:", remaining)
