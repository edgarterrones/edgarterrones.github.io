# Edgar C Terrones
# 10/23/25
# P4HW1
# List and Loops

scores = []
num_scores = int(input("How many scores do you want to enter? ")) #asks how many scores and stores it


for i in range(num_scores): #range is however many scores user wants to input
    score = int(input(f"Enter score #{i + 1}: ")) #asks user to input score with prompt
    if 0 <= score <= 100: #checks if score is valid
        scores.append(score) #stores the score in the list
    else:
        print("INVALID Score entered!!!")
        print("Score should be between 0 and 100")          
        score = int(input(f"Enter Score #{i + 1} again:")) #allows user to input score again

avg_grade = sum(scores)/len(scores)
# saves the average and assigns letter grade
if avg_grade >= 90:
    letter_grade = "A"

elif avg_grade >= 80:
    letter_grade = "B"

elif avg_grade >= 70:
    letter_grade = "C"
    
elif avg_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("-----------Results-----------")
print(f"{"Lowest Grade:":<20}", min(scores))  #Gets you the lowest score in the list
print(f"{"Modified List":<20}", scores) #list
print(f"{"Average:":<20}", f"{sum(scores)/len(scores):.2f}") #Gets the average score of the grades in the list
print(f"{"Grade:":<20}", letter_grade) #gives letter grade
print("-----------------------------")


    


