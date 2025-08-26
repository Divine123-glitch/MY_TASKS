# UNILAG Admission Checker
# Step 1: Collect the needed input from users 
# Step 2: Check for eligibility based on department
# Step 3: Print formatted output


department_subjects = {
    "science": ['Biology', 'Chemistry', 'Physics'],
    "commercial": ['Economics', 'Commerce', 'Accounting'],
    "humanity": ['Literature', 'Government', 'History']
}


student_input = {
    "name": input("Enter your full name: ").title(),
    "age": int(input("Enter your age: ")),
    "department": input("Enter your department (science, commercial, humanity): ").strip().lower(),
    "utme": int(input("Enter your UTME score: "))
}

while student_input["department"] not in department_subjects:
    print("Invalid department! Please choose science, commercial, or humanity.")
    student_input["department"] = input("Enter your department (science, commercial, humanity): ").strip().lower()


subjects = ['Maths', 'English'] + department_subjects[student_input["department"]]
student_input['grade'] = {
    subject: input(f"Enter {subject} grade in O'Level Result: ").strip().upper() for subject in subjects
}


name = student_input["name"]
age = student_input["age"]
department = student_input["department"]
utme = student_input["utme"]
grade = student_input["grade"]


eligibility = (
    age > 15 and 
    utme > 199 and 
    all(grade[subj] in ['A', 'B', 'C'] for subj in subjects)
)
print(f"Eligibility: {eligibility}")


cut_mark = {"A": 64, "B": 44, "C": 24}
total_score = sum(cut_mark.get(grade[subj], 0) for subj in subjects)
admission_status = total_score >= 200


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