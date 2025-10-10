# Edgar C Terrones
# 10/7/25
# P3HW1
# BUGFIX


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1:'))
mod_2 = float(input('Enter grade for Module 2:'))
mod_3 = float(input('Enter grade for Module 3:'))
mod_4 = float(input('Enter grade for Module 4:'))
mod_5 = float(input('Enter grade for Module 5:'))
mod_6 = float(input('Enter grade for Module 6:'))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades
avg_grade = sum(grades)/6


print("-----------Results-----------")
print(f"{"Lowest Grade:":<20}", min(grades))  #Gets you the lowest score in the list
print(f"{"Highest Grade:":<20}", max(grades)) #Gets you the highest score in the list
print(f"{"Sum of Grades:":<20}", sum(grades)) #Adds all the scores in the list
print(f"{"Average:":<20}", f"{sum(grades)/6:.2f}") #Gets the average score of the grades in the list
print("-----------------------------")

# determine letter grade for average


if avg_grade >= 90:
    print('Your grade is: A')

elif avg_grade >= 80:
 print('Your grade is: B')

elif avg_grade >= 70:
   print('Your grade is: C')

elif avg_grade >= 60:
   print('Your grade is: D')

else:
    print('Your grade is: F') # TO DO: finish this





