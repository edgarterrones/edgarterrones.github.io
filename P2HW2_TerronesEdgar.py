# Edgar C Terrones
# 10/7/25
# P2HW2
# List

module_one = float(input("Enter grade for Module 1: "))

module_two = float(input("Enter grade for Module 2: "))

module_three = float(input("Enter grade for Module 3: "))

module_four = float(input("Enter grade for Module 4: "))

module_five = float(input("Enter grade for Module 5: "))

module_six = float(input("Enter grade for Module 6: "))

test_grades = [module_one, module_two, module_three, module_four, module_five, module_six]

print("-----------Results-----------")
print(f"{"Lowest Grade:":<20}", min(test_grades))
print(f"{"Highest Grade:":<20}", max(test_grades))
print(f"{"Sum of Grades:":<20}", sum(test_grades))
print(f"{"Average:":<20}", f"{sum(test_grades)/6:.2f}")
print("-----------------------------")

