# Edgar C Terrones
# 10/10/25
# P3HW2
# Employee pay

employee_name = input("Enter employee's name: ")
hours_worked = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

#establish variables for overtime
over_time = 0
over_time_pay = 0 

#calculates overtime hours
if hours_worked > 40:
    over_time = hours_worked - 40
    over_time_pay = over_time * pay_rate * 1.5
    regular_hours = 40
else:
    regular_hours = hours_worked

#calculate pay

reg_pay = regular_hours * pay_rate

gross_pay = reg_pay + over_time_pay

    

print("------------------------------") #30 dashes
print("Employee's name: ")

print("Hours Worked        Pay Rate            OverTime          Overtime Pay" \
"           RegHour Pay          Gross Pay")
print("--------------------------------------------------------------" \
"------------------------------------------------------")

print(f"{hours_worked:<20}{pay_rate:<20}{over_time:<20}${over_time_pay:<20.2f}${reg_pay:<20.2f}${gross_pay:.2f}")

