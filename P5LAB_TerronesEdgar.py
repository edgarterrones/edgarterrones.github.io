# Edgar C Terrones
# 11/10/25
# P5LAB
# CHANGE

import random
def disperse_change(change):
    #Converting the value to an interger
    change = round(change*100)


    #Determine how much of each are needed
    num_dollars = change//100
    change = change-(num_dollars*100)

    num_quarters = change//25
    change= change-(num_quarters *25)
    
    num_dimes= change//10
    change = change-(num_dimes *10)

    num_nickels = change//5
    change = change-(num_nickels*5)

    num_pennies = change
    #Display coins needed
    if num_dollars>0:
        if num_dollars == 1:
          print(f'{num_dollars} dollar')
        else:
          print(f'{num_dollars} dollars')
    if num_quarters >0:
        if num_quarters==1:
            print(f'{num_quarters} quarter')
        else:
            print(f'{num_quarters} quarters')
    if num_nickels>0:
        if num_nickels == 1:
          print(f'{num_nickels} nickel')
        else: 
          print(f'{num_nickels} nickels')
    if num_dimes>0:
        if num_dimes == 1:
          print(f'{num_dimes} dime')
        else:
          print(f'{num_dimes} dimes')
    if num_pennies>0:
        if num_dimes == 1:
          print(f'{num_pennies} pennies')
        else:
          print(f'{num_pennies} pennies')
    
def main():
    

    #Genereate the amount owed
    DEBT= round(random.uniform(0.01, 100.00), 2)
    print(f'You owe ${DEBT:.2f}')

    # create variable for money put into machine
    money_in = float(input("How much cash will you put in the self-checkout?"))

    #Calculate change owed
    change= money_in -DEBT
    print(f'Change is: ${change:.2f}')

    #call the function
    disperse_change(change)
#Call the main function
main()