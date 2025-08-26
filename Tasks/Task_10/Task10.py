# UNILAG Admission Checker
# Step 1: Collect the needed input from users with basic exception handling
# Step 2: Check for eligibility based on department
# Step 3: Print formatted output

department_subjects = {
    "science": ['Biology', 'Chemistry', 'Physics'],
    "commercial": ['Economics', 'Commerce', 'Accounting'],
    "humanity": ['Literature', 'Government', 'History']
}

# Collect student input with exception handling
student_input = {}
try:
    student_input["name"] = input("Enter your full name: ").title()
    if not student_input["name"]:
        raise ValueError("Name cannot be empty")

    student_input["age"] = int(input("Enter your age: "))
    if student_input["age"] < 10 or student_input["age"] > 100:
        raise ValueError("Age must be between 10 and 100")

    student_input["department"] = input("Enter your department (science, commercial, humanity): ").strip().lower()
    while student_input["department"] not in department_subjects:
        print("Invalid department! Please choose science, commercial, or humanity.")
        student_input["department"] = input("Enter your department (science, commercial, humanity): ").strip().lower()

    student_input["utme"] = int(input("Enter your UTME score: "))
    if student_input["utme"] < 0 or student_input["utme"] > 400:
        raise ValueError("UTME score must be between 0 and 400")

    subjects = ['Maths', 'English'] + department_subjects[student_input["department"]]
    student_input['grade'] = {}
    valid_grades = ['A', 'B', 'C']
    for subject in subjects:
        grade = input(f"Enter {subject} grade in O'Level Result: ").strip().upper()
        if grade not in valid_grades:
            raise ValueError(f"Grade for {subject} must be one of {valid_grades}")
        student_input['grade'][subject] = grade

except ValueError as e:
    print(f"Error: {e}")
    exit(1)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
    exit(0)

# Extract student input for processing
name = student_input["name"]
age = student_input["age"]
department = student_input["department"]
utme = student_input["utme"]
grade = student_input["grade"]

# Check eligibility
eligibility = (
    age > 15 and 
    utme > 199 and 
    all(grade[subj] in ['A', 'B', 'C'] for subj in subjects)
)

# Calculate total score
cut_mark = {"A": 64, "B": 44, "C": 24}
total_score = sum(cut_mark.get(grade[subj], 0) for subj in subjects)
admission_status = total_score >= 200

# Print formatted output
print("-" * 45, "Admission Checker", "-" * 45)
print(f"Candidate: {name}")
print(f"Age: {age}")
print(f"Department: {department.title()}")
print(f"UTME Score: {utme}")
print("O'Level Result:")
for subj in subjects:
    print(f"{subj}: {grade[subj]}")
print(f"Total Score: {total_score}")
print(f"Admission Status: {'Admitted' if admission_status else 'Not Admitted'}")
print("-" * 109)