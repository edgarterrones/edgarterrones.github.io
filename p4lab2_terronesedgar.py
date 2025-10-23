# Edgar C Terrones
# 10/22/25
# P4LAB2
# MULTIPLICATION TABLE

run_again = "yes"

while run_again != "no": #start loop
    num = int(input("Enter an integer: "))
    if num >= 0: #runs all non negative numbers
       for i in range(1, 13):
            print(f"{num} x {i} = {num * i}")
    else: #negative numbers
        print("This program does not handle negative values")
    run_again = input("Would you like to run the program again? ")
print("Exiting program... ")


