# Student score tracker
# Step 0: Create two empty lists
# Step 1: Ask the user for the three student names
# Step 2: Ask for their score
# Step 3: Store the results in two lists (one for names, one for scores)
# Step 4: Print a formatted output showing Name — Score, aligned neatly.

Student_name = []
Student_score = []
for i in range(3):
    name = input(f"Enter the name of student {i+1}: ")
    Student_name.append(name)

for i in range(3):
    score = float(input(f"Enter score for {Student_name[i]}: "))
    Student_score.append(score)

print("\nStudents Scores: ")
print("{:<20} {:<10}".format("Name", "Score"))
print("*" * 35)
for i in range(3):
    print("{:<20} {:<10}".format(Student_name[i], Student_score[i]))
