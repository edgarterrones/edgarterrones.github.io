# Edgar C Terrones
# 10/29/25
# P4HW2
# Employee pay loop

overtime_total = 0 
regular_pay_total = 0
gross_pay_total = 0
num_employees = 0

# Input employee name
employee_name = input("Enter employee name or 'Done' to terminate: ")


while employee_name != 'Done': #start loop
    pay_rate = float(input("Enter pay rate: "))
    hours_worked = float(input("Enter hours worked: "))

    #calculates overtime hours
    if hours_worked > 40:               
        over_time = hours_worked - 40
        over_time_pay = over_time * (pay_rate * 1.5)
 
        #calculate pay
        reg_pay = 40 * pay_rate
        gross_pay = reg_pay + over_time_pay
    else:
        over_time = 0
        over_time_pay = 0
        reg_pay = hours_worked*pay_rate
        gross_pay = reg_pay
                
    print("------------------------------") #30 dashes
    print("Employee's name: ")

    print("Hours Worked        Pay Rate            OverTime          Overtime Pay" \
    "           RegHour Pay          Gross Pay")
    print("--------------------------------------------------------------" \
    "--------------------------------------------")

    print(f"{hours_worked:<20}{pay_rate:<20}{over_time:<20}${over_time_pay:<20.2f}${reg_pay:<20.2f}${gross_pay:.2f}")   

    # Update totals
    regular_pay_total += reg_pay
    overtime_total += over_time_pay
    gross_pay_total += gross_pay
    num_employees += 1

    # next employee or done
    employee_name = input("Enter another employee name or 'Done' to terminate: ")

# Display results


print(f"Total number of Employees: {num_employees}")
print(f"Total amount paid for overtime: ${overtime_total:.2f}")
print(f"Total amount paid for regular hours: ${regular_pay_total:.2f}")
print(f"Total amount paid for gross: ${gross_pay_total:.2f}")

