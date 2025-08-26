# Student Score Tracker
# Step 0: Create two empty lists
# Step 1: Ask the user for the three student names and scores
# Step 2: Store the results in two lists (one for names, one for scores)
# Step 3: Print a formatted output showing Name — Score, aligned neatly.

Student_name = []
Student_score = []

try:
    for i in range(3):
        name = input(f"Enter the name of student {i+1}: ").strip().title()
        if not name:
            raise ValueError(f"Name of student {i+1} cannot be empty")

        score_input = input(f"Enter score for {name}: ").strip()
        if not score_input:
            raise ValueError(f"Score for {name} cannot be empty")
        score = float(score_input)
        if score < 0 or score > 100:
            raise ValueError(f"Score for {name} must be between 0 and 100")

        Student_name.append(name)
        Student_score.append(score)

except ValueError as e:
    print(f"Error: {e}")
    exit(1)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
    exit(0)

# Print formatted output
print("\n--- Students Scores ---")
print("{:<20} {:<10}".format("Name", "Score"))
print("*" * 35)
if Student_name:
    for i in range(len(Student_name)):
        print("{:<20} {:<10}".format(Student_name[i], Student_score[i]))
else:
    print("No students registered.")