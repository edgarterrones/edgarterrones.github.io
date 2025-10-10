# Edgar C Terrones
# 10/10/25
# P3LAB
# CHANGE

# get value from user
change = float(input("Enter an amount of money as a float: $"))

#convert the value to an integer
change = round(change * 100)


#determine how many dollars are needed
num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickles = change // 5
change = change - (num_nickles * 5)

num_pennies = change

#print out the needed values
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")

if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} Quarter")
    else:
        print(f"{num_quarters} Quarters")

if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")

if num_nickles > 0:
    if num_nickles == 1:
        print(f"{num_nickles} Nickle")
    else:
        print(f"{num_nickles} Nickles")

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} Pennies")
if change == 0:
    print("No change")